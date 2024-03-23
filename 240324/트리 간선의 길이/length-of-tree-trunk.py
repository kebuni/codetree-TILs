import sys
sys.setrecursionlimit(100000)

N = int(input())

edge = [[] for i in range(N)]
dist_list = [0 for i in range(N)]
visited = [False for i in range(N)]

for i in range(N-1):
    a, b, d = map(int,input().split())
    edge[a-1].append((b-1,d))
    edge[b-1].append((a-1,d))

############################

def dfs(cur):
    for next, dist in edge[cur]:
        if not visited[next]:
            dist_list[next] = dist_list[cur] + dist
            push(next)
            dfs(next)
    return

def push(cur):
    visited[cur] = True
    return

############################

push(0)
dfs(0)

max_idx = 0
max_dist = 0
for i in range(N):
    if dist_list[i] > max_dist:
        max_idx = i
        max_dist = dist_list[i]

visited = [False for i in range(N)]
dist_list = [0 for i in range(N)]
push(max_idx)
dfs(max_idx)

max_idx = 0
max_dist = 0
for i in range(N):
    if dist_list[i] > max_dist:
        max_idx = i
        max_dist = dist_list[i]

print(max_dist)