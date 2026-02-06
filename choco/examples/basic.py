
"""Basic choco example showing `Events`, `on`, `after`, and queued emissions.

This example inserts the local `choco/src` directory onto `sys.path` so it runs
from the repository checkout without installing the package.
"""

import pathlib
import sys

# Make choco package importable from the local checkout (choco/src)
HERE = pathlib.Path(__file__).resolve()
SRC = HERE.parents[1] / "src"
sys.path.insert(0, str(SRC))

from choco import Events, on, after


def main() -> None:
	events = Events()

	# Register names (optional, used for introspection)
	events.register("greet")
	events.register("first")
	events.register("second")

	@on(events, "greet")
	def say_hello(event):
		# Access event payload as mapping
		name = event.get("name", "world")
		print(f"ON: Hello {name} (event: {event.name})")


	@after(events, "greet")
	def after_hello(event):
		print(f"AFTER: Completed greeting for {event['name']}")

	# Simple emit
	print("-- Simple emit --")
	events.emit("greet", name="Alice")

	# Demonstrate queued emission: one handler queues another emission
	@on(events, "first")
	def first_handler(event):
		print("ON first -> queueing 'second' emission")
		events.emit_later("second", info="from first")

	@after(events, "second")
	def after_second(e):
		print(f"AFTER second -> received: {e.data}")

	print("\n-- Queued emission demo --")
	events.emit("first")

	# Show safe exception handling: an exception in an @after action is logged,
	# but does not prevent other after actions from running.
	@after(events, "greet")
	def flaky_after(event):
		print("AFTER flaky -> about to raise")
		raise RuntimeError("simulated after failure")

	@after(events, "greet")
	def resilient_after(event):
		print("AFTER resilient -> runs despite other after failing")
	

	print("\n-- After-action exception handling demo --")
	events.emit("greet", name="Bob")


if __name__ == "__main__":
	main()
