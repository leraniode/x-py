from logically import Condition
from logically import Rule
from logically import Decision
from logically.types import Context

# Condition and Rule
cond = Condition("flag", lambda v: v is True)
rule = Rule("flag_rule", [cond])

# Action for Decision
def action(ctx: Context):
    print(f"Flag is {ctx['flag']}")
    return ctx["flag"]

# Decision
decision = Decision(
    name="check_flag",
    rule=rule,
    action=action
)

ctx: Context = {"flag": True}
result = decision.execute(ctx)  # prints "Flag is True"
print(result)  # True