"""
Condition module - represents a logical requirement.

A Condition holds a rule that can be evaluated later.
It does not run automatically.
"""

from dataclasses import dataclass
from typing import Callable, Optional, Any

@dataclass(frozen=True, slots=True)
class Condition:
    """
    Condition represents a logical requirement.

    Attributes:
        name: Name of the condition.
        rule: A callable that returns True/False when evaluated.
        description: Optional text describing the condition.
    
    Example:
        >>> cond = Condition(name="is_authenticated", rule=lambda user: user is not None)
        >>> cond.rule("Alice")
        True
    """
    name: str
    rule: Callable[[Any], bool]
    description: Optional[str] = None

    def __str__(self) -> str:
        return self.name