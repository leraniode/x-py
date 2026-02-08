"""
Intent module - represents what is intended.

An Intent describes a goal or purpose in a system.
It does not execute actions or mutate state.
"""

from dataclasses import dataclass
from typing import Optional, Mapping, Any

@dataclass(frozen=True, slots=True)
class Intent:
    """
    Intent represents a logical intention.

    Attributes:
        name: Name of the intent.
        description: Optional text describing the intent.
        metadata: Optional additional metadata.
    
    Example:
        >>> intent = Intent(name="save_data", description="Save user info")
        >>> print(intent)
        save_data
    """
    name: str
    description: Optional[str] = None
    metadata: Optional[Mapping[str, Any]] = None

    def __str__(self) -> str:
        return self.name