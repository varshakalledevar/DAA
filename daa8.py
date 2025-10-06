def create_matrix(n,edges):
    adj=[[0]*n for i in range(n)]
    for u,v in edges:
        adj[u][v]=adj[u][v]=1
    return adj

n,e=map(int, input("enter vertices and edges").split())
edges=[tuple(map(int,input().split())) for _ in range(e)]
adj=create_matrix(n,edges)
print("\n adjency matrix:")
for row in adj:
    print(*row)