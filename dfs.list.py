def dfs_adj_list(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)  
    print(start, end=" ")
    for adjacent in graph[start]:
        if adjacent not in visited:
            dfs_adj_list(graph, adjacent, visited)


graph = {
   0:[1, 2, 3],
   1:[0, 3],
   2:[0, 3],
   3:[0, 1, 2]
}

print("DFS using Adjacency List:")
dfs_adj_list(graph, 0)  