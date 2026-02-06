"""
Choco - Simple, explicit event engine for Python experiments.

Part of Leraniode X experimental projects.
"""

from .event import Event
from .events import Events
from .action import on, after

__all__ = ["Event", "Events", "on", "after"]
__version__ = "0.1.0"