N, K = map(int, input().split())

edge = [[] for i in range(N)]
visited = [False for i in range(N)]
parent = [-1 for i in range(N)]
depth = [0 for i in range(N)]

arr = list(map(int, input().split()))

def dfs(cur):
    for next in edge[cur]:
        if not visited[next]:
            parent[next] = cur
            depth[next] = depth[cur] + 1
            push(next)
            dfs(next)
    return

def push(cur):
    visited[cur] = True
    return

parent_idx = 0
i = 1
while i < N:
    start = arr[i]
    j = i
    while j < N:
        end = arr[j]
        if j+1 < N and arr[j+1] == end+1:
            j += 1
        else:
            break

    #print(i,j)

    for idx in range(i,j+1):
        edge[parent_idx].append(idx)
        edge[idx].append(parent_idx)
    i = j + 1
    parent_idx += 1

# print("edge",edge)

target_idx = arr.index(K)
# print("target_idx",target_idx)

push(0)
dfs(0)

# print("parent",parent)
# print("depth",depth)

depth_of_target = depth[target_idx]
parent_of_target = parent[target_idx]
ans = 0
for i in range(N):
    if i == depth_of_target:
        continue

    if parent[i] == -1:
        continue

    if parent[i] != parent_of_target and parent[parent[i]] == parent[parent_of_target]:
        ans += 1

print(ans)