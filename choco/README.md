<p align="left">
  <img
    src="https://raw.githubusercontent.com/leraniode/.github/main/assets/images/chocoproductimage.png"
    alt="choco product image"
    width="300"
    style="border-radius: 15px;"
  />
</p>

# Choco 🍫

![experimental-leraniode](https://raw.githubusercontent.com/leraniode/.github/main/assets/badges/experimentalleraniode.svg)
![choco-flavoured-leraniode](https://raw.githubusercontent.com/leraniode/.github/main/assets/badges/chocoflavouredleraniode.svg)

**Choco** is a simple, explicit event system for Python experiments.

It is designed for:
- small systems
- tooling
- internal frameworks
- prototyping event-driven logic

Choco is part of **X**, the experimental Leraniode workspace.

---

## Features

- 🚀 **Fast** — minimal overhead, no magic
- 🎯 **Explicit** — events and actions are clear and predictable
- 🧱 **Immutable Events** — safe, structured event data
- 🔗 **Composable** — build your own abstractions on top

---

## Quick Start

### Try it Yourself

```python
from choco import Events, on, after

events = Events()

@on(events, "user_login")
def greet(event):
    print(f"Hello {event['username']}")

@after(events, "user_login")
def audit(event):
    print("Login event processed")

events.emit("user_login", username="Alice")
```

Output:
```
Hello Alice
Login event processed
```

### Event Data

Event data is passed as keyword arguments and accessed via dictionary-style access:

```python
@on(events, "purchase")
def handle(event):
    print(event["item"])
    print(event.get("price", 0))
```

## Error Handling

- Exceptions in @on handlers stop execution and are raised
- Exceptions in @after handlers are logged and execution continues

This keeps failures visible while allowing cleanup logic to run.

## Installation

```bash
pip install git+https://github.com/leraniode/x-py.git#subdirectory=choco
```

## Requirements
- Python 3.10+
- No external dependencies

## License

MIT License. See [LICENSE](../LICENSE) for details.