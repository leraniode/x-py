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
        self._queued_emissions.append((event_name, data))