# ---------------------------------------------
# Depth-First Search (DFS)
# Directed Graph Based on Given Diagram
# ---------------------------------------------

import streamlit as st

st.image("LabReport_BSD2513_#1.jpg")

# Directed graph from the question
graph = {
    'A': ['B', 'D'],
    'B': ['C', 'E', 'G'],
    'C': ['A'],
    'D': ['C'],
    'E': ['H'],
    'F': [],
    'G': ['H', 'F'],
    'H': ['F']
}

visited = []  # track visited nodes

def dfs(visited, graph, node, order):
    if node not in visited:
        visited.append(node)
        order.append(node)

        # Sort neighbors alphabetically before exploring
        for neighbour in sorted(graph[node]):
            dfs(visited, graph, neighbour, order)


# Run DFS starting from A
order = []
dfs(visited, graph, 'A', order)

# Display results
st.header("DFS Traversal Order")
st.write(" → ".join(order))

st.header("Visited Nodes")
st.write(visited)
