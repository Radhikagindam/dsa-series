def dfs_adj_matrix(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for adjacent in range(len(graph)):
        if graph[start][adjacent] == 1 and adjacent not in visited:
            dfs_adj_matrix(graph, adjacent, visited)


graph = [
    [1, 1, 1, 1],  
    [1, 0, 0, 1],  
    [1, 0, 0, 1],  
    [1, 1, 1, 1]  
    ]
print("\nDFS using Adjacency Matrix:")
dfs_adj_matrix(graph, 0)