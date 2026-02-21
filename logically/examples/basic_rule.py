from logically import Condition
from logically import Rule
from logically.types import Context

# Define a simple condition
cond_a = Condition("age_check", lambda v: v >= 18)

# Define a rule using the condition
rule = Rule(
    name="adult_rule",
    conditions=[cond_a],
    description="Check if user is an adult"
)

# Context dictionary
context: Context = {"age_check": 20}

# Evaluate rule
result = rule.evaluate(context)
print(f"Rule passed? {result}")  # True