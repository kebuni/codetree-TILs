N, M = map(int,input().split())

edge = [[] for i in range(N+1)]
visited = [False for i in range(N+1)]
dist_list = [0 for i in range(N+1)]

def get_dist(x,y):
    global visited, dist_list
    visited = [False for i in range(N+1)]
    dist_list = [0 for i in range(N+1)]
    push(x,0)
    dfs(x,0)
    return dist_list[y]

def dfs(cur,cur_dist):
    for next, dist in edge[cur]:
        if not visited[next]:
            push(next,cur_dist+dist)
            dfs(next,cur_dist+dist)
    return

def push(x,dist):
    dist_list[x] = dist
    visited[x] = True
    return

for i in range(N-1):
    x, y, dist = map(int,input().split())
    edge[x].append((y,dist))
    edge[y].append((x,dist))

for i in range(M):
    x, y = map(int,input().split())
    print(get_dist(x,y))