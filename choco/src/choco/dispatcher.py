"""
Dispatcher functions for Choco Internally.

The Dispatcher is responsible for managing the flow of events and their associated actions. It takes care of executing "on" actions before the event is processed and "after" actions after the event is processed. It also handles any exceptions that may occur during the execution of actions, ensuring that one failing action does not prevent others from running.
"""

import sys
import traceback
from typing import Any

from .event import Event
from .handler import Handler


class Dispatcher:
    def __init__(self, handler: Handler) -> None:
        self._handler = handler
        self._queued_emissions: list[tuple[str, dict[str, Any]]] = []

    def dispatch(self, event_name: str, data: dict[str, Any]) -> None:
        """Dispatch ``event_name`` with ``data`` synchronously.

        Creates an :class:`Event` for ``event_name`` and runs all bound
        "on" actions first. If an "on" action raises an exception the
        exception is printed and re-raised to surface the failure. After
        running "on" actions, all "after" actions are executed; exceptions
        raised by "after" actions are logged but do not stop subsequent
        after-actions or queued emissions.
        """

        event = Event(event_name, data)

        for action in self._handler.get_on_actions(event_name):
            try:
                action(event)
            except Exception:
                print(
                    f"[choco] @on action '{action.__name__}' failed for '{event_name}'",
                    file=sys.stderr,
                )
                traceback.print_exc()
                raise

        for action in self._handler.get_after_actions(event_name):
            try:
                action(event)
            except Exception:
                print(
                    f"[choco] @after action '{action.__name__}' failed for '{event_name}'",
                    file=sys.stderr,
                )
                traceback.print_exc()

        while self._queued_emissions:
            name, payload = self._queued_emissions.pop(0)
            self.dispatch(name, payload)

    def queue_emission(self, event_name: str, data: dict[str, Any]) -> None:
        """Queue an emission to be dispatched after the current dispatch

        This is useful when handlers want to schedule events to be emitted
        once the current event processing completes. Queued emissions are
        processed in FIFO order by the running dispatcher.
        """

        self._queued_emissions.append((event_name, data))