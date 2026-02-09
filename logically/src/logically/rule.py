"""
Rule module - encapsulates a logical rule.

A Rule evaluates a set of conditions and produces a boolean outcome.
"""

from dataclasses import dataclass
from typing import Callable, Optional, Any, List
from .condition import Condition
from .types import Context

@dataclass(frozen=True, slots=True)
class Rule:
    """
    Rule evaluates one or more conditions.

    Attributes:
        name: Name of the rule
        conditions: List of Condition objects
        evaluator: Callable that takes list of Condition results and returns bool
        description: Optional description
    """
    name: str
    conditions: List[Condition]
    evaluator: Optional[Callable[[List[bool]], bool]] = None
    description: Optional[str] = None

    def evaluate(self, context: Context) -> bool:
        results = [
            cond.rule(context.get(cond.name)) for cond in self.conditions
        ]
        evaluator = self.evaluator or (lambda r: all(r))
        return evaluator(results)
    
