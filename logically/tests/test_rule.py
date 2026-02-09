from logically import Condition
from logically import Rule
from logically.types import Context


def test_rule_all_conditions_true():
    is_admin = Condition("is_admin", lambda v: v is True)
    is_active = Condition("is_active", lambda v: v is True)

    rule = Rule(
        name="admin_access",
        conditions=[is_admin, is_active],
    )

    context: Context = {
        "is_admin": True,
        "is_active": True,
    }

    assert rule.evaluate(context) is True


def test_rule_one_condition_false():
    is_admin = Condition("is_admin", lambda v: v is True)
    is_active = Condition("is_active", lambda v: v is True)

    rule = Rule(
        name="admin_access",
        conditions=[is_admin, is_active],
    )

    context: Context = {
        "is_admin": True,
        "is_active": False,
    }

    assert rule.evaluate(context) is False


def test_rule_custom_evaluator():
    a = Condition("a", lambda v: v is True)
    b = Condition("b", lambda v: v is True)

    rule = Rule(
        name="any_true",
        conditions=[a, b],
        evaluator=lambda results: any(results),
    )

    context: Context = {"a": False, "b": True}
    assert rule.evaluate(context) is True