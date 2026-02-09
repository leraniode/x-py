<p align="left">
  <img src="https://raw.githubusercontent.com/leraniode/.github/main/assets/images/logicallyproductimage.png"
       alt="logically product image"
       width="300" />
</p>

# logically 🤔

![experimental-leraniode](https://raw.githubusercontent.com/leraniode/.github/main/assets/badges/experimentalleraniode.svg)
![logically-smart-leraniode](https://raw.githubusercontent.com/leraniode/.github/main/assets/badges/logicallysmartleraniode.svg)

**logically** is a logic-construction toolkit for building clean, composable, and inspectable
logic units in Python.

It helps you express **intent**, **conditions**, **rules**, and **decisions**
without coupling them to execution, parsing, or side effects.

Part of **Leraniode X** (experimental projects).

---

## Why logically?

Most systems mix:
- conditions
- control flow
- side effects
- execution

**logically separates them**.

You define *what* logic means — not *how* it runs.

---

## Core Concepts

### Condition
A single logical check.

```python
from logically import Condition

is_adult = Condition(
    name="age",
    rule=lambda v: v >= 18,
    description="User must be an adult"
)
```

### Rule

A group of conditions evaluated together.

```python
from logically import Rule

access_rule = Rule(
    name="access_allowed",
    conditions=[is_adult],
)
```

Rules return boolean outcomes.

### Decision

A rule paired with an optional action.

```python
from logically import Decision

decision = Decision(
    name="grant_access",
    rule=access_rule,
    action=lambda ctx: "Access granted"
)

result = decision.execute(age=21)
```

### Graph (advanced)

Graphs allow composing rules and decisions into inspectable logical flows.

> Graphs describe structure — not execution engines.

## Design Principles

- Explicit > implicit
- No magic execution
- No hidden state
- No framework lock-in
- Composable by the user

## Installation

```bash
pip install git+https://github.com/leraniode/x-py.git#subdirectory=logically
```

## License

MIT License. See [`License`](../LICENSE) file