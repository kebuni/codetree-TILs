N = int(input())
edge = [[] for i in range(N+1)]
visited = [False for i in range(N+1)]
parent = [0 for i in range(N+1)]
num = [0 for i in range(N+1)]
for i in range(2,N+1):
    t, a, p = map(int,input().split())
    edge[i].append(p)
    edge[p].append(i)
    parent[i] = p
    if t == 1:
        num[i] = a
    else:
        num[i] = -a 

#########################

def push(x):
    visited[x] = True
    return

def dfs(x):
    for next in edge[x]:
        if not visited[next]:
            push(next)
            dfs(next)

    for next in edge[x]:
        if parent[next] == x:
            if arr[next] > 0:
                arr[x] += arr[next]
    
    return


#########################

push(1)
dfs(1)
print(arr[1])