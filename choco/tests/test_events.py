"""Tests for core event system."""

import sys
import pathlib
import pytest

# Ensure the package in `choco/src` is importable during tests
ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))

from src.choco import Events, Event, on, after


def test_basic_event():
    """Test basic event emission and handling."""
    events = Events()
    results = []

    @on(events, "test")
    def handler(event):
        results.append(event.data)

    events.emit("test", value=42)

    assert len(results) == 1
    assert results[0] == {"value": 42}


def test_multiple_handlers():
    """Test multiple handlers for same event."""
    events = Events()
    results = []

    @on(events, "test")
    def handler1(event):
        results.append("handler1")

    @on(events, "test")
    def handler2(event):
        results.append("handler2")

    events.emit("test")

    assert results == ["handler1", "handler2"]


def test_event_data_access():
    """Test accessing event data via dictionary-style access."""
    events = Events()
    result = {}

    @on(events, "user_login")
    def handler(event):
        result["username"] = event["username"]
        result["age"] = event["age"]

    events.emit("user_login", username="alice", age=30)

    assert result["username"] == "alice"
    assert result["age"] == 30


def test_event_data_get_method():
    """Test accessing event data via get method with defaults."""
    events = Events()
    result = {}

    @on(events, "user_login")
    def handler(event):
        result["username"] = event.get("username", "unknown")
        result["email"] = event.get("email", "no-email@example.com")

    events.emit("user_login", username="alice")

    assert result["username"] == "alice"
    assert result["email"] == "no-email@example.com"


def test_after_action():
    """Test after action execution."""
    events = Events()
    results = []

    @on(events, "test")
    def on_handler(event):
        results.append("on")

    @after(events, "test")
    def after_handler(event):
        results.append("after")

    events.emit("test")

    assert results == ["on", "after"]


def test_exception_in_on_action():
    """Test that exception in on action is raised."""
    events = Events()

    @on(events, "test")
    def failing_handler(event):
        raise ValueError("Test error")

    with pytest.raises(ValueError, match="Test error"):
        events.emit("test")


def test_exception_in_after_action():
    """Test that exception in after action doesn't prevent after actions from running."""
    events = Events()
    results = []

    @after(events, "test")
    def failing_handler(event):
        results.append("after1")
        raise ValueError("Test error")

    @after(events, "test")
    def success_handler(event):
        results.append("after2")

    # After actions don't raise, they just log
    events.emit("test")

    assert results == ["after1", "after2"]


def test_event_immutability():
    """Test that Event is immutable."""
    event = Event("test", {"key": "value"})

    with pytest.raises(Exception):  # FrozenInstanceError
        event.name = "modified" # type: ignore


def test_registered_events():
    """Test registering events."""
    events = Events()

    events.register("user_login")
    events.register("user_logout")

    assert "user_login" in events.registered_events
    assert "user_logout" in events.registered_events