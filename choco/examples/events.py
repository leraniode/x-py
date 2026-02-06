"""
Example: basic event handling with Choco.
"""

from choco import Events, Event, on, after

events = Events()

@on(events, "user.login")
def greet(event: Event):
    print(f"User logged in: {event['username']}")

@after(events, "user.login")
def audit(event: Event):
    print("Audit log:", event.data)

# Emit
events.emit("user.login", username="Alice")