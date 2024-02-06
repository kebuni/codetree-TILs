#####################

def dfs(n):
    global visited, conneted_with_1
    for i in range(1,N+1):
        if graph[n][i] and not visited[i]:
            conneted_with_1.append(i)
            visited[i] = True
            dfs(i)

    return

#####################

N, M = map(int,input().split())

graph = [[0 for i in range(N+1)]for j in range(N+1)]
visited = [False for i in range(N+1)]
conneted_with_1 = []

for i in range(M):
    r,c = map(int,input().split())
    graph[r][c] = 1
    graph[c][r] = 1

visited[1] = True
dfs(1)
#print(conneted_with_1)
print(len(conneted_with_1))