from collections import deque


def BFS(graph,start_i):
    num_of_node=len(graph)
    visited=[False]*num_of_node
    queue=deque([start_i])
    res=[]

    while queue:
        node=queue.popleft()

        if not visited[node]:
            visited[node]=True
            res.append(node)

            for neighbor in range(num_of_node):
                if graph[node][neighbor]==1 and not visited[neighbor]:
                    queue.append(neighbor)

    print(f'BFS traversal: {res}')




graph=  [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 1],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
]

start_node=0

BFS(graph,start_node)
