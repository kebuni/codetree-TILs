N = int(input())

edges = [[] for i in range(N+1)]
visited = [False for i in range(N+1)]
parent = [0 for i in range(N+1)]

for i in range(N-1):
    a, b = map(int,input().split())
    edges[a].append(b)
    edges[b].append(a)

def traverse(cur):
    visited[cur] = True
    for next in edges[cur]:
        if not visited[next]:
            parent[next] = cur
            traverse(next)
    return

traverse(1)

for i in range(2,N+1):
    print(parent[i])