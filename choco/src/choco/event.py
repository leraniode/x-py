"""
Event system for Choco.

Events are immutable objects that represent something that happened in the system. They have a name and a data dictionary that can contain any relevant information about the event.
Handlers can bind actions to events, which are functions that will be called when the event is triggered. There are two types of actions: "on" actions, which are called before the event is processed, and "after" actions, which are called after the event is processed.

Example usage:
```python
from choco import Event, Handler
def on_user_registered(event: Event) -> None:
    print(f"User registered: {event['username']}")
handler = Handler()
handler.bind_on("user_registered", on_user_registered)
event = Event(name="user_registered", data={"username": "alice"})
for action in handler.get_on_actions(event.name):
    action(event)
```

Is choco sweet? We'll love to hear your feedback! If you have any questions, suggestions, or want to contribute, please join our community on GitHub or Discord.
"""

from typing import Any
from dataclasses import dataclass


@dataclass(frozen=True)
class Event:
    name: str
    data: dict[str, Any]

    def __post_init__(self) -> None:
        if not isinstance(self.data, dict):
            raise TypeError(f"Event.data must be dict, got {type(self.data)}")

    def __getitem__(self, key: str) -> Any:
        """Return the value for ``key`` from the event data.

        Allows event instances to be accessed like mappings: ``event["foo"]``.
        Raises ``KeyError`` if the key is not present.
        """

        return self.data[key]

    def get(self, key: str, default: Any = None) -> Any:
        """Return the value for ``key`` if present, otherwise ``default``.

        This mirrors the mapping ``get`` API and is a safe way to fetch
        optional values from the event payload.
        """

        return self.data.get(key, default)