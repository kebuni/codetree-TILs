import sys
sys.setrecursionlimit(100000)
INT_MAX = sys.maxsize

N, D = map(int,input().split())

edge = [[] for i in range(N)]
real_edge = [[] for i in range(N)]
dist_list = [0 for i in range(N)]
real_dist_list = [0 for i in range(N)]
visited = [False for i in range(N)]

for i in range(N-1):
    a, b, c = map(int,input().split())
    edge[a-1].append((b-1,1))
    edge[b-1].append((a-1,1))
    real_edge[a - 1].append((b - 1, c))
    real_edge[b - 1].append((a - 1, c))

############################

def dfs(cur):
    for i in range(len(edge[cur])) :
        next,dist = edge[cur][i]
        _,real_dist = real_edge[cur][i]
        if not visited[next]:
            dist_list[next] = dist_list[cur] + dist
            real_dist_list[next] = real_dist_list[cur] + real_dist
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
max_dist = (-INT_MAX, INT_MAX)
for i in range(N):
    if (dist_list[i],- real_dist_list[i]) > max_dist:
        max_idx = i
        max_dist = (dist_list[i],- real_dist_list[i])

# print(max_idx)
# print(dist_list)

visited = [False for i in range(N)]
dist_list = [0 for i in range(N)]
real_dist_list = [0 for i in range(N)]
push(max_idx)
dfs(max_idx)

max_idx = 0
max_dist = (-INT_MAX, INT_MAX)
for i in range(N):
    if (dist_list[i],- real_dist_list[i]) > max_dist:
        max_idx = i
        max_dist = (dist_list[i],- real_dist_list[i])

# print(max_idx)
# print(dist_list)
# print(real_dist_list)

if real_dist_list[max_idx] % D:
    print(real_dist_list[max_idx] // D + 1)
else:
    print(real_dist_list[max_idx] // D)