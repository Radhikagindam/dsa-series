def create_adjacency_list(v, edges):
    adjlist = []
    
    # Initialize empty lists for each vertex
    for i in range(v):
        adjlist.append([])
    
    # Fill adjacency list
    for n, m in edges:
        adjlist[n].append(m)
        adjlist[m].append(n)  # because it's an undirected graph
    
    # Sort each adjacency list
    for adj in adjlist:
        adj.sort()
    
    return adjlist
v = 5
edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]

adj_list = create_adjacency_list(v, edges)
print(adj_list)

