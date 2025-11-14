import streamlit as st

# ---------------------------------------------
# Breadth-First Search (BFS)
# Directed Graph Based on Given Diagram
# ---------------------------------------------

# SAFE Windows path (use raw string r"..." or double slashes)
st.image(r"C:\Users\stayw\Desktop\AI SEM 5\lab report\LabReport_BSD2513_#1.jpg")

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

visited = []
queue = []

def bfs(visited, graph, start_node):
    order = []   # store traversal to display in Streamlit

    visited.append(start_node)
    queue.append(start_node)

    while queue:
        current = queue.pop(0)
        order.append(current)

        for neighbour in sorted(graph[current]):
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

    return order


# Run BFS
order = bfs(visited, graph, 'A')

# Display BFS results in Streamlit
st.header("BFS Traversal Order")
st.write(" → ".join(order))

st.header("Visited Nodes")
st.write(visited)

