def bfs_matrix(graph, start):
    n = len(graph)  
    queue = [start]  
    visited = [False] * n  
    visited[start] = 1

    while queue:
        node = queue.pop(0)  
        print(node, end=" ")  

        for adjacent in range(n):   
            if graph[node][adjacent] != False and visited[adjacent] ==False:  
                visited[adjacent] = 1   
                queue.append(adjacent)  


graph = [
    [0, 1, 1, 1],  
    [1, 0, 0, 1],  
    [1, 0, 0, 1],  
    [1, 1, 1, 0] 
]

bfs_matrix(graph, 0)