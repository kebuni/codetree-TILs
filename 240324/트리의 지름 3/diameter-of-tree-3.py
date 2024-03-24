N = int(input())

edge = [[] for i in range(N+1)]
visited = [False for i in range(N+1)]
dist_list = [0 for i in range(N+1)]

for i in range(N-1):
    a, b, d = map(int,input().split())
    edge[a].append((b,d))
    edge[b].append((a,d))

def dfs(cur):
    visited[cur] = True
    for next, dist in edge[cur]:
        if not visited[next]:
            dist_list[next] = dist_list[cur] + dist
            dfs(next)

dfs(1)
max_dist = 0
max_idx = -1
for i in range(1,N+1):
    if dist_list[i] > max_dist:
        max_dist = dist_list[i]
        max_idx = i

visited = [False for i in range(N+1)]
dist_list = [0 for i in range(N+1)]

dfs(max_idx)
dist_list.sort(reverse=True)
print(dist_list[1])