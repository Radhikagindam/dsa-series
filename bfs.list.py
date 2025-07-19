def bfs_list(graph, start):
    n = len(graph)
    queue = [start]
    visited = [False] * n
    visited[start] = True

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for adjacent in graph[node]:
            if not visited[adjacent]:
                visited[adjacent] = True
                queue.append(adjacent)


graph = {
    0:[1, 2, 3],
    1:[0, 3],
    2:[0, 3],
    3:[0, 1, 2]
}

bfs_list(graph, 0)