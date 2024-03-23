import sys
sys.setrecursionlimit(100000)
N = int(input())

edge = [[] for i in range(N+1)]
visited = [False for i in range(N+1)]
depth_list = [-1 for i in range(N+1)]
is_leaf = [False for i in range(N+1)]

def dfs(cur,depth):
    children_num = 0
    for next in edge[cur]:
        if not visited[next]:
            children_num += 1
            push(next,depth+1)
            dfs(next,depth+1)
    if not children_num:
        is_leaf[cur] = True

    return

def push(cur,depth):
    depth_list[cur] = depth
    visited[cur] = True
    return

for i in range(N-1):
    a,b  = map(int,input().split())
    edge[a].append(b)
    edge[b].append(a)

push(1,0)
dfs(1,0)
# print(depth_list)
# print(is_leaf)
sum = 0
for i in range(1,N+1):
    if is_leaf[i]:
        sum += depth_list[i]
print((sum) % 2)