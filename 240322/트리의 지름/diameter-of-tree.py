N = int(input())

visited = [False for i in range(N+1)]
edge = [[] for i in range(N+1)]
parent = [0 for i in range(N+1)]
dist = [0 for i in range(N+1)]

for i in range(N-1):
    x, y, d = map(int,input().split())
    edge[x].append((y,d))
    edge[y].append((x,d))

def push(cur,d):
    visited[cur] = True
    dist[cur] = d
    return

def traverse(cur, cur_d):
    for next, d in edge[cur]:
        if not visited[next]:
            parent[next] = cur
            push(next, cur_d + d)
            traverse(next, cur_d + d)
    return

push(1,0)
traverse(1,0)
# print(dist)

max_dist = 0
max_node = 0
for x in range(1,N+1):
    if dist[x] > max_dist:
        max_dist = dist[x]
        max_node = x
# print(max_node)
# print(max_dist)

visited = [False for i in range(N+1)]
push(max_node,0)
traverse(max_node, 0)
#print(dist)

max_dist = 0
max_node = 0
for x in range(1,N+1):
    if dist[x] > max_dist:
        max_dist = dist[x]
        max_node = x
#print(max_node)
print(max_dist)