from logically import Graph

# Create graph
g = Graph()
g.add_node("start")
g.add_node("middle")
g.add_node("end")

# Connect nodes
g.add_edge("start", "middle")
g.add_edge("middle", "end")

# Inspect neighbors
print("Start neighbors:", g.neighbors("start"))  # ['middle']
print("Graph:", g)