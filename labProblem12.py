def depth_first_search(grp,start,n,visited3):

    visited3[start]=True
    print(start,end=' ')

    for neighbor in range(n):
        if not visited3[neighbor] and grp[start][neighbor]==1:
            depth_first_search(grp,neighbor,n,visited3)

n3=int(input('Enter Number of vertices'))

graph=[]

print("Enter the adjacency matrix (space-separated values for each row):")

for i in range(n3):
    row=list(map(int,input().split()))
    graph.append(row)




# graph= [
#     [0, 1, 0, 1, 0],
#     [1, 0, 1, 0, 1],
#     [0, 1, 0, 1, 0],
#     [1, 0, 1, 0, 1],
#     [0, 1, 0, 1, 0]
# ]

n1 = len(graph)
visited2=[False]*n1
depth_first_search(graph,0,n1,visited2)
