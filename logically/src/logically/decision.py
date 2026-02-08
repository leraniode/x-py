"""
Decision module - represents an outcome based on rules.

A Decision can execute different actions depending on rule evaluation.
"""

from dataclasses import dataclass, field
from typing import Callable, Optional, Any
from .rule import Rule
from .types import Context

@dataclass(frozen=True, slots=True)
class Decision:
    """
    Decision evaluates a Rule and triggers an optional action.

    Attributes:
        name: Name of the decision
        rule: Rule object to evaluate
        action: Optional callable to run if rule evaluates True
        description: Optional description
    """
    name: str
    rule: Rule
    action: Optional[Callable[[Context], Any]] = None
    description: Optional[str] = None

    def execute(self, context: Context) -> Any | None:
        if self.rule.evaluate(context) and self.action:
            return self.action(context)
        return None

    def __str__(self) -> str:
        return self.name