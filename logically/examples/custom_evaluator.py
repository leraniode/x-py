from logically import Condition
from logically import Rule
from logically.types import Context

# Two conditions
c1 = Condition("x", lambda v: v > 5)
c2 = Condition("y", lambda v: v < 10)

# Rule with custom evaluator (any condition passing is enough)
rule = Rule(
    name="any_pass_rule",
    conditions=[c1, c2],
    evaluator=lambda results: any(results)
)

context: Context = {"x": 2, "y": 8}
print("Rule passed?", rule.evaluate(context))  # True