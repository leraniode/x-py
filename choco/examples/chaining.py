"""
Example: chaining events via bind().
"""

from choco import Events, on, after

events = Events()

@after(events, "start")
def trigger_second(event):
    print("Start event:", event.data)
    # Queue a second event
    events.emit_later("second", value=event["value"] * 2)

@after(events, "second")
def handle_second(event):
    print("Second event value:", event["value"])

events.emit("start", value=5)