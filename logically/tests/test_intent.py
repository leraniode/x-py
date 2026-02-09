from logically import Intent


def test_intent_creation():
    intent = Intent(
        name="user-auth",
        description="Represents user authentication intent",
    )

    assert intent.name == "user-auth"
    assert intent.description == "Represents user authentication intent"


def test_intent_string_representation():
    intent = Intent(
        name="payment-flow",
        description="Handles payment logic",
    )

    assert str(intent) == "payment-flow"