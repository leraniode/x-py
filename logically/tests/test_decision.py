from logically import Condition
from logically import Rule
from logically import Decision
from logically.types import Context


def test_decision_executes_action_with_context():
    received: dict = {}

    def action(ctx: Context):
        received["value"] = ctx["value"]
        return "ok"

    condition = Condition("enabled", lambda v: v is True)
    rule = Rule(
        name="enabled_rule",
        conditions=[condition],
    )

    decision = Decision(
        name="run_when_enabled",
        rule=rule,
        action=action,
    )

    context: Context = {
        "enabled": True,
        "value": 42,
    }

    result = decision.execute(context)

    assert result == "ok"
    assert received["value"] == 42


def test_decision_does_not_execute_when_rule_fails():
    called = False

    def action(ctx: Context):
        nonlocal called
        called = True

    condition = Condition("enabled", lambda v: v is True)
    rule = Rule("enabled_rule", [condition])

    decision = Decision(
        name="run_when_enabled",
        rule=rule,
        action=action,
    )

    context: Context = {"enabled": False}
    result = decision.execute(context)

    assert result is None
    assert called is False


def test_decision_without_action_is_safe():
    condition = Condition("flag", lambda v: v is True)
    rule = Rule("flag_rule", [condition])

    decision = Decision(
        name="no_action",
        rule=rule,
        action=None,
    )

    context: Context = {"flag": True}
    assert decision.execute(context) is None