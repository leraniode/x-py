"""
logically - Declarative logic library for Python

This package provides the building blocks for defining logic:
- Intents
- Conditions
- Rules (coming later)
- Decisions (coming later)

Each API component is immutable, descriptive, and independent.

Part of Leraniode X experimental projects
"""

from .intent import Intent
from .condition import Condition
from .rule import Rule
from .decision import Decision
from .graph import Graph
from .errors import LogicallyError, ConditionError, RuleError, DecisionError

__all__ = [
    "Intent",
    "Condition",
    "Rule",
    "Decision",
    "Graph",
    "LogicallyError",
    "ConditionError",
    "RuleError",
    "DecisionError"
]
__version__ = "0.1.0"