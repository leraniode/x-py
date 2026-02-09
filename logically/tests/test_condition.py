import pytest
from logically import Condition


def test_condition_true():
    cond = Condition(
        name="is_even",
        rule=lambda x: x % 2 == 0,
        description="Checks if number is even",
    )

    assert cond.rule(4) is True
    assert cond.rule(3) is False


def test_condition_name():
    cond = Condition(name="exists", rule=lambda x: x is not None)
    assert cond.name == "exists"
