"""
Event system for Choco.

This module provides the core event system for the Choco framework, allowing you to define events, bind actions to those events, and dispatch them. The main components are:
- `Event`: An immutable object representing an event with a name and associated data.
- `Handler`: Manages the binding of actions to events, allowing you to specify "on" and "after" actions.
- `Dispatcher`: Responsible for executing the bound actions when an event is dispatched, handling any exceptions that may occur during execution.
- `Events`: A high-level interface that combines the functionality of the Handler and Dispatcher, allowing you to register events, emit them, and bind actions in a convenient way.

Example usage:
```python
from choco import Events
events = Events()
def on_user_registered(event):
    print(f"User registered: {event['username']}")
def after_user_registered(event):
    print(f"Welcome email sent to: {event['username']}")
events.register("user_registered")
events.bind_on_action("user_registered", on_user_registered)
events.bind_after_action("user_registered", after_user_registered)
events.emit("user_registered", username="alice")
```

Is choco sweet? We'll love to hear your feedback! If you have any questions, suggestions, or want to contribute, please join our community on GitHub or Discord.
"""

from typing import Any

from .handler import Handler
from .dispatcher import Dispatcher


class Events:
    def __init__(self) -> None:
        self._handler = Handler()
        self._dispatcher = Dispatcher(self._handler)
        self._registered: set[str] = set()

    def register(self, event_name: str) -> str:
        """Register an event name so it appears in ``registered_events``.

        Returns the registered ``event_name``. Registration is idempotent.
        """

        self._registered.add(event_name)
        return event_name

    def emit(self, event_name: str, **data: Any) -> None:
        """Emit ``event_name`` immediately with the provided keyword data.

        Synchronously dispatches the event to any bound "on" and "after"
        actions via the internal :class:`Dispatcher`.
        """

        self._dispatcher.dispatch(event_name, data)

    def emit_later(self, event_name: str, **data: Any) -> None:
        """Schedule ``event_name`` to be emitted after the current dispatch.

        The event is queued on the :class:`Dispatcher` and will be dispatched
        once the currently running dispatch completes.
        """

        self._dispatcher.queue_emission(event_name, data)

    def bind_on_action(self, event_name: str, action) -> None:
        """Bind an ``action`` to run as an "on" action for ``event_name``.

        The ``action`` should accept a single :class:`Event` argument.
        """

        self._handler.bind_on(event_name, action)

    def bind_after_action(self, event_name: str, action) -> None:
        """Bind an ``action`` to run as an "after" action for ``event_name``.

        The ``action`` will be executed after "on" actions and the main
        dispatch logic. The action should accept a single :class:`Event`
        argument.
        """

        self._handler.bind_after(event_name, action)

    @property
    def registered_events(self) -> set[str]:
        """Return a copy of the set of registered event names.

        The returned set is a shallow copy and can be inspected safely by
        callers without modifying the internal registration state.
        """

        return self._registered.copy()