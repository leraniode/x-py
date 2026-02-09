import pytest
from logically import (
    LogicallyError,
    ConditionError,
    RuleError,
    DecisionError,
)


def test_base_error_is_exception():
    err = LogicallyError("base")
    assert isinstance(err, Exception)
    assert str(err) == "base"


def test_condition_error_inherits_logically_error():
    err = ConditionError("condition failed")
    assert isinstance(err, LogicallyError)


def test_rule_error_inherits_logically_error():
    err = RuleError("rule failed")
    assert isinstance(err, LogicallyError)


def test_decision_error_inherits_logically_error():
    err = DecisionError("decision failed")
    assert isinstance(err, LogicallyError)


def test_errors_can_be_raised_and_caught():
    with pytest.raises(ConditionError):
        raise ConditionError("bad condition")