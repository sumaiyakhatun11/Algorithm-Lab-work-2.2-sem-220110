import heapq

def dijkstra_matrix(graph, start, end):
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    pq = [(0, start)]  # (distance, node)
    parent = [-1] * n

    while pq:
        dist, node = heapq.heappop(pq)

        for neighbor in range(n):
            if graph[node][neighbor] > 0:  # If there is an edge
                new_dist = dist + graph[node][neighbor]
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
                    parent[neighbor] = node

    # Reconstruct the shortest path
    path = []
    curr = end
    while curr != -1:
        path.append(chr(ord('A') + curr))  # Convert index to letter
        curr = parent[curr]
    path.reverse()

    return distances[end], path

# Graph Representation using Adjacency Matrix
#   A  B  C  D  E
graph = [
    [0, 5, 3, 0, 0],  # A
    [5, 0, 1, 3, 0],  # B
    [3, 1, 0, 2, 6],  # C
    [0, 3, 2, 0, 4],  # D
    [0, 0, 6, 4, 0]   # E
]

start_node = 0  # A
end_node = 4    # E
shortest_distance, shortest_path = dijkstra_matrix(graph, start_node, end_node)

print(f"Shortest Distance: {shortest_distance}")
print(f"Shortest Path: {' -> '.join(shortest_path)}")
