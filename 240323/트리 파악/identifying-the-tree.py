import sys
sys.setrecursionlimit(100000)
N = int(input())
#print(N)
edge = [[] for i in range(N+1)]
visited = [False for i in range(N+1)]
# depth_list = [-1 for i in range(N+1)]
# is_leaf = [False for i in range(N+1)]
result = 0
#print(N)
for i in range(N-1):
    a, b = map(int,input().split())
    #print(a,b)
    edge[a].append(b)
    edge[b].append(a)

###################################3

def dfs(cur,depth):
    global result
    children_num = 0
    for next in edge[cur]:
        if not visited[next]:
            children_num += 1
            push(next,depth+1)
            dfs(next,depth+1)
    if not children_num:
        result += depth
    return

def push(cur,depth):
    #depth_list[cur] = depth
    visited[cur] = True
    return

##############################3

push(1,0)
dfs(1,0)
# print(depth_list)
# print(is_leaf)
print((result) % 2)