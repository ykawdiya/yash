from collections import deque

# Initialize an empty graph
graph = {}

# Function to add an edge to the graph
def add_edge(u, v):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)  # Undirected graph

# Recursive DFS
def dfs(node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=' ')
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs(neighbor, visited)

# BFS using queue
def bfs(start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Menu-driven interface
def main():
    while True:
        print("\n--- Graph Menu ---")
        print("1. Add edge")
        print("2. Display graph")
        print("3. DFS traversal")
        print("4. BFS traversal")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            u = input("Enter first vertex: ")
            v = input("Enter second vertex: ")
            add_edge(u, v)
            print(f"Edge added between {u} and {v}")
        elif choice == '2':
            print("Graph adjacency list:")
            for node in graph:
                print(f"{node} -> {graph[node]}")
        elif choice == '3':
            start = input("Enter starting vertex for DFS: ")
            if start in graph:
                print("DFS traversal:", end=' ')
                dfs(start)
                print()
            else:
                print("Start vertex not found in graph.")
        elif choice == '4':
            start = input("Enter starting vertex for BFS: ")
            if start in graph:
                print("BFS traversal:", end=' ')
                bfs(start)
                print()
            else:
                print("Start vertex not found in graph.")
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()