def create_matrix(n, edges, directed):
    adj = [[0] * n for i in range(n)]
    for u, v in edges:
        adj[u][v] = 1
        if not directed:
                adj[v][u] = 1
    return adj
def degrees(adj):
    n = len(adj)
    indeg = [0] * n
    outdeg = [0] * n
    for i in range(n):
        for j in range(n):
          if adj[i][j]:
            outdeg[i] += 1
            indeg[j] += 1
    return indeg,outdeg
n, e = map(int, input("enter vertices and edges:").split())
directed = input("directed (yes/no):").lower() == "yes"
edges = [tuple(map(int, input().split())) for i in range(e)]
adj = create_matrix(n, edges, directed)
indeg, outdeg = degrees(adj)
print("\n adjacency matrix:")
for row in adj: print(*row)
print("\n vertex in dgree out degree")
for i in range(n):
    print(i, " " * (7 - len(str(i))),indeg[i], " " * (9 - len(str(indeg[i]))),outdeg[i])
