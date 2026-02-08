"""
Graph module - simple directed graph for logical flows.
"""

from collections import defaultdict
from typing import Any, Dict, List

class Graph:
    """
    Directed graph representing nodes and edges.

    Example:
        g = Graph()
        g.add_node("start")
        g.add_node("end")
        g.add_edge("start", "end")
    """
    
    def __init__(self) -> None:
        self._nodes: set[str] = set()
        self._edges: Dict[str, List[str]] = defaultdict(list)

    def add_node(self, node: str) -> None:
        self._nodes.add(node)

    def add_edge(self, from_node: str, to_node: str) -> None:
        if from_node not in self._nodes or to_node not in self._nodes:
            raise ValueError("Both nodes must exist before adding edge")
        self._edges[from_node].append(to_node)

    def neighbors(self, node: str) -> List[str]:
        return self._edges.get(node, [])

    def __str__(self) -> str:
        return f"Graph(nodes={list(self._nodes)}, edges={dict(self._edges)})"