"""
Action module for Choco.

Defines decorators for binding actions to events.
An action is a function that takes an Event as an argument and performs some operation when the event is triggered.

Example usage:
```python
from choco import Events, on

events = Events()

@on(events, "my_event")
def my_action(event):
    print(f"Event {event.name} triggered with data: {event.data}")
events.emit("my_event", data="Hello, World!")
```
In this example, the `my_action` function is decorated with `@on(events, "my_event")`, which binds it to the "my_event" event. When "my_event" is triggered, `my_action` will be called with the event data.

Is choco sweet? We'll love to hear your feedback! If you have any questions, suggestions, or want to contribute, please join our community on GitHub or Discord.
"""

from typing import Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from .events import Events
    from .event import Event

ActionFunc = Callable[["Event"], None]


def on(events: "Events", event_name: str):
    def decorator(action: ActionFunc) -> ActionFunc:
        """Bind ``action`` as an "on" action for ``event_name`` on ``events``.

        The decorated function will be called with an :class:`Event` instance
        when ``event_name`` is emitted via the given ``events`` instance.
        """
        events.bind_on_action(event_name, action)
        return action
    return decorator


def after(events: "Events", event_name: str):
    def decorator(action: ActionFunc) -> ActionFunc:
        """Bind ``action`` as an "after" action for ``event_name`` on ``events``.

        The decorated function will be called with an :class:`Event` instance
        after the event has been processed (i.e., after any "on" actions
        and the main event dispatch logic have run).
        """
        events.bind_after_action(event_name, action)
        return action
    return decorator