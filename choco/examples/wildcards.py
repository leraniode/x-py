"""
Example: wildcard event handlers.
"""

from choco import Events, on, after

events = Events()

@on(events, "user.*")
def all_user_events(event):
    print(f"[Wildcard] {event.name}", event.data)

@on(events, "user.logout")
def logout_handler(event):
    print("Goodbye:", event["username"])

events.emit("user.login", username="Alice")
events.emit("user.logout", username="Bob")