"""
Handler module for managing event actions in Choco.

Handlers allow you to bind functions (actions) to specific events. When an event is triggered, the corresponding actions will be executed in the order they were bound. There are two types of actions: "on" actions, which are executed before the event is processed, and "after" actions, which are executed after the event is processed.
"""

from typing import Callable
from collections import defaultdict

from .event import Event

ActionFunc = Callable[[Event], None]


class Handler:
    def __init__(self) -> None:
        self._on_actions: dict[str, list[ActionFunc]] = defaultdict(list)
        self._after_actions: dict[str, list[ActionFunc]] = defaultdict(list)

    def bind_on(self, event_name: str, action: ActionFunc) -> None:
        self._on_actions[event_name].append(action)

    def bind_after(self, event_name: str, action: ActionFunc) -> None:
        self._after_actions[event_name].append(action)

    def get_on_actions(self, event_name: str) -> list[ActionFunc]:
        return list(self._on_actions.get(event_name, []))

    def get_after_actions(self, event_name: str) -> list[ActionFunc]:
        return list(self._after_actions.get(event_name, []))