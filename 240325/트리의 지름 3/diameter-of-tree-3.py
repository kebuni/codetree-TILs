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
max_idx1 = -1
for i in range(1,N+1):
    if dist_list[i] > max_dist:
        max_dist = dist_list[i]
        max_idx1 = i

visited = [False for i in range(N+1)]
dist_list = [0 for i in range(N+1)]

dfs(max_idx1)
max_dist = 0
max_idx2 = -1
for i in range(1,N+1):
    if dist_list[i] > max_dist:
        max_dist = dist_list[i]
        max_idx2 = i

candidate1 = 0
for i in range(1,N+1):
    if i == max_idx2:
        continue
    candidate1 = max(candidate1,dist_list[i])

visited = [False for i in range(N+1)]
dist_list = [0 for i in range(N+1)]
dfs(max_idx2)

dist_list.sort(reverse=True)
candidate2 = dist_list[1]

print(max(candidate1,candidate2))