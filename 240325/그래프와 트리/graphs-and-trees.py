N, M = map(int,input().split())

edge = [[] for i in range(N+1)]
visited = [False for i in range(N+1)]
connected = set()
ans = 0

for i in range(M):
    a, b = map(int,input().split())
    edge[a].append(b)
    edge[b].append(a)

def dfs(cur):
    for next in edge[cur]:
        if not visited[next]:
            push(next)
            dfs(next)

def push(cur):
    visited[cur] = True
    connected.add(cur)
    return

for i in range(1,N+1):
    if not visited[i]:
        connected.clear()
        push(i)
        dfs(i)
        edge_num = 0
        for member in connected:
            for next in edge[member]:
                if next in connected:
                    edge_num += 1
        if edge_num//2 == len(connected)-1:
            ans += 1

print(ans)