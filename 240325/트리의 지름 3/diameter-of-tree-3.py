import sys
sys.setrecursionlimit(100000)
N = int(input())

edge = [[] for i in range(N+1)]
visited = [False for i in range(N+1)]
dist_list = [0 for i in range(N+1)]
max_dist = 0
last_node = 0
a, b, ans = 0, 0, 0

for i in range(N-1):
    a, b, d = map(int,input().split())
    edge[a].append((b,d))
    edge[b].append((a,d))

def dfs(cur,ignore):
    global max_dist, last_node
    visited[cur] = True
    for next, dist in edge[cur]:
        if not visited[next]:
            dist_list[next] = dist_list[cur] + dist

            if dist_list[next] > max_dist and next != ignore:
                max_dist = dist_list[next]
                last_node = next

            dfs(next,ignore)

dfs(1,-1)
a = last_node

visited = [False for i in range(N+1)]
dist_list = [0 for i in range(N+1)]
max_dist = -1

dfs(a,-1)
b = last_node

visited = [False for i in range(N+1)]
dist_list = [0 for i in range(N+1)]
max_dist = -1

dfs(a,b)
ans = max(ans,max_dist)

visited = [False for i in range(N+1)]
dist_list = [0 for i in range(N+1)]
max_dist = -1

dfs(b,a)
ans = max(ans,max_dist)

print(ans)