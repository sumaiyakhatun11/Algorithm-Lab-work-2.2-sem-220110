def greedy_tsp(adj):
    n=len(adj)
    visited=[False]*n
    total_distance1=0
    current_home=0
    path1=[current_home]
    visited[current_home]=True

    for _ in range(n-1):
        min_distance=float('inf')
        nearest_home=-1
        for i in range(n):
            if not visited[i] and adj[current_home][i]<min_distance:

                min_distance=adj[current_home][i]
                nearest_home=i

        visited[nearest_home]=True
        total_distance1+=min_distance
        path1.append(nearest_home)
        current_home=nearest_home

    total_distance1 += adj[current_home][path1[0]]
    path1.append(path1[0])
    return path1,total_distance1











adjacency_matrix = [
    [0, 10, 15, 20, 25, 30],
    [10, 0, 35, 25, 30, 5],
    [15, 35, 0, 30, 5, 10],
    [20, 25, 30, 0, 15, 10],
    [25, 30, 5, 15, 0, 20],
    [30, 5, 10, 10, 20, 0]
]

# Run the greedy TSP algorithm
path, total_distance = greedy_tsp(adjacency_matrix)

# Displaying the results
print("Optimal path:", path)
print("Total distance:", total_distance)