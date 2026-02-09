import pytest
from logically import Graph


def test_graph_initial_state():
    g = Graph()
    assert str(g) == "Graph(nodes=[], edges={})"


def test_add_node():
    g = Graph()
    g.add_node("start")

    assert "start" in g._nodes


def test_add_multiple_nodes():
    g = Graph()
    g.add_node("a")
    g.add_node("b")

    assert g._nodes == {"a", "b"}


def test_add_edge_success():
    g = Graph()
    g.add_node("start")
    g.add_node("end")

    g.add_edge("start", "end")

    assert g.neighbors("start") == ["end"]


def test_add_edge_requires_existing_nodes():
    g = Graph()
    g.add_node("start")

    with pytest.raises(ValueError):
        g.add_edge("start", "end")


def test_neighbors_empty_when_no_edges():
    g = Graph()
    g.add_node("solo")

    assert g.neighbors("solo") == []


def test_graph_string_representation():
    g = Graph()
    g.add_node("a")
    g.add_node("b")
    g.add_edge("a", "b")

    text = str(g)
    assert "nodes" in text
    assert "edges" in text