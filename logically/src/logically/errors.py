"""
Errors module - logically-specific exceptions.
"""

class LogicallyError(Exception):
    """Base exception for logically"""

class ConditionError(LogicallyError):
    """Raised when a condition fails or is invalid"""

class RuleError(LogicallyError):
    """Raised when a rule evaluation fails"""

class DecisionError(LogicallyError):
    """Raised when a decision execution fails"""