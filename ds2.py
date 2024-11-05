from collections import deque

class Graph:
    def __init__(self):
        # Dictionary to store the adjacency list of the directed graph
        self.graph = {}

    def add_edge(self, u, v):
        """Add a directed edge from node u to node v."""
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)  # Only one direction for directed graph

    def bfs(self, start):
        """Perform Breadth-First Search (BFS) starting from the given node."""
        visited = set()  # Set to keep track of visited nodes
        queue = deque([start])  # Queue for BFS
        bfs_result = []  # To store the order of traversal

        while queue:
            node = queue.popleft()  
            if node not in visited:
                visited.add(node)
                bfs_result.append(node)
                # Add all unvisited neighbors to the queue
                for neighbor in self.graph.get(node, []):
                    if neighbor not in visited:
                        queue.append(neighbor)

        return bfs_result

    def dfs(self, start):
        """Perform Depth-First Search (DFS) starting from the given node."""
        visited = set()  # Set to keep track of visited nodes
        dfs_result = []  # To store the order of traversal

        def dfs_recursive(node):
            """Helper function to perform DFS using recursion."""
            visited.add(node)
            dfs_result.append(node)
            # Visit all unvisited neighbors
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(start)  # Start the DFS from the starting node
        return dfs_result

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)

# Perform BFS and DFS from a starting node (e.g., node 0)
start_node = 0
print("BFS Traversal:", g.bfs(start_node))
print("DFS Traversal:", g.dfs(start_node))
