class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = []    # Adjacency list to hold the graph

    def add_edge(self, u, v, w):
        """Add an edge to the graph."""
        self.graph.append((u, v, w))

    def dijkstra(self, src):
        """Implement Dijkstra's algorithm."""
        dist = [float("inf")] * self.V
        dist[src] = 0
        visited = [False] * self.V

        for _ in range(self.V):
            min_dist = float("inf")
            min_index = 0

            for v in range(self.V):
                if not visited[v] and dist[v] < min_dist:
                    min_dist = dist[v]
                    min_index = v

            visited[min_index] = True

            for u, v, w in self.graph:
                if u == min_index and not visited[v] and dist[min_index] + w < dist[v]:
                    dist[v] = dist[min_index] + w

        return dist

    def floyd_warshall(self):
        """Implement Floyd-Warshall algorithm."""
        dist = [[float("inf")] * self.V for _ in range(self.V)]

        for u, v, w in self.graph:
            dist[u][v] = w

        for i in range(self.V):
            dist[i][i] = 0

        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        return dist

    def bellman_ford(self, src):
        """Implement Bellman-Ford algorithm."""
        dist = [float("inf")] * self.V
        dist[src] = 0

        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Check for negative-weight cycles
        for u, v, w in self.graph:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                raise ValueError("Graph contains a negative-weight cycle")

        return dist
    def display_distances(self, distances):
        """Display the result distances in a readable format."""
        print("Vertex distances:")
        for i, distance in enumerate(distances):
            print(f"Distance from source to vertex {i}: {distance}")

    def display_floyd_matrix(self, matrix):
        """Display the Floyd-Warshall distance matrix."""
        print("Distance matrix (Floyd-Warshall):")
        for row in matrix:
            print(" ".join(f"{d:7}" if d != float("inf") else " " for d in row))

# Example usage
# Create a graph instance
n=int(input("Enter the number of vertices: "))
g = Graph(5)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 3)
g.add_edge(1, 2, 1)
g.add_edge(1, 3, 2)
g.add_edge(2, 1, 4)
g.add_edge(2, 3, 8)
g.add_edge(2, 4, 2)
g.add_edge(3, 4, 7)
g.add_edge(4, 3, 9)
source_vertex=int(input("Enter the source vertex: "))
distances_dijkstra = g.dijkstra(source_vertex)
g.display_distances(distances_dijkstra)
floyd_matrix = g.floyd_warshall()
g.display_floyd_matrix(floyd_matrix)
distances_bellman_ford = g.bellman_ford(source_vertex)
g.display_distances(distances_bellman_ford)

