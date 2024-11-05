import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = [[] for _ in range(vertices)]  # Adjacency list for Prim's
        self.edges = []  # Edge list for Kruskal's

    def add_edge(self, u, v, w):
        """Add an edge to the graph."""
        # For Prim's MST (adjacency list representation)
        self.graph[u].append((w, v))
        self.graph[v].append((w, u))
        
        # For Kruskal's MST (edge list representation)
        self.edges.append((w, u, v))

    def prim_mst(self):
        """Implement Prim's algorithm to find MST."""
        mst_cost = 0
        visited = set()
        min_heap = [(0, 0)]  # Start from node 0 with a cost of 0
        mst_edges = []

        while min_heap and len(visited) < self.V:
            weight, u = heapq.heappop(min_heap)
            if u in visited:
                continue
            visited.add(u)
            mst_cost += weight
            mst_edges.append(u)

            for w, v in self.graph[u]:
                if v not in visited:
                    heapq.heappush(min_heap, (w, v))

        # Check if all nodes are visited (graph is connected)
        if len(visited) != self.V:
            print("Graph is disconnected; Prim's MST can't be computed for all nodes.")
        else:
            print("Prim's MST cost:", mst_cost)
            print("Vertices in MST (using Prim's):", mst_edges)

    def kruskal_mst(self):
        """Implement Kruskal's algorithm to find MST."""
        # Sort edges by weight
        self.edges.sort()
        parent = list(range(self.V))
        rank = [0] * self.V

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                if rank[root_x] > rank[root_y]:
                    parent[root_y] = root_x
                elif rank[root_x] < rank[root_y]:
                    parent[root_x] = root_y
                else:
                    parent[root_y] = root_x
                    rank[root_x] += 1

        mst_cost = 0
        mst_edges = []

        for w, u, v in self.edges:
            if find(u) != find(v):
                union(u, v)
                mst_cost += w
                mst_edges.append((u, v, w))

        print("Kruskal's MST cost:", mst_cost)
        print("Edges in MST (using Kruskal's):", mst_edges)

# Sample Connected Graph
# Create a graph instance with 5 vertices
g = Graph(5)

# Adding edges to ensure the graph is connected
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)
g.add_edge(1, 4, 10)
g.add_edge(3, 4, 7)

# Running Prim's Algorithm
print("Running Prim's Algorithm:")
g.prim_mst()

# Running Kruskal's Algorithm
print("\nRunning Kruskal's Algorithm:")
g.kruskal_mst()
