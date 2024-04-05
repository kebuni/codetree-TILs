import sys
sys.setrecursionlimit(110000)

N = int(input())
edge = [[] for i in range(N+1)]
parent = [0 for i in range(N+1)]
visited = [False for i in range(N+1)]
dp = [[0,1] for i in range(N+1)]

for i in range(N-1):
    a, b = map(int,input().split())
    edge[a].append(b)
    edge[b].append(a)

#####################

def push(x):
    visited[x] = True
    return

def dfs(x):
    for next in edge[x]:
        if not visited[next]:
            parent[next] = x
            push(next)
            dfs(next)

    for next in edge[x]:
        if parent[next] == x:
            dp[x][0] += dp[next][1]
            dp[x][1] += min(dp[next][0],dp[next][1])

    return

#####################

push(1)
dfs(1)
print(min(dp[1][0],dp[1][1]))