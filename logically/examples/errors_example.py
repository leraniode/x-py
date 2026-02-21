from logically import ConditionError, RuleError, DecisionError

try:
    raise ConditionError("Condition failed!")
except ConditionError as e:
    print(e)

try:
    raise RuleError("Rule evaluation failed!")
except RuleError as e:
    print(e)

try:
    raise DecisionError("Decision execution failed!")
except DecisionError as e:
    print(e)