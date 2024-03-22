import sys

sys.setrecursionlimit(100000)

N = 10000
M = int(input())

edge = [[] for i in range(N + 1)]
visited = [False for i in range(N + 1)]
active_node = [False for i in range(N + 1)]
candidate_node = [True for i in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    edge[a].append(b)
    active_node[a] = True
    active_node[b] = True
    candidate_node[b] = False

final_activate_node = []
final_candidate_node = []

for i in range(1, N + 1):
    if active_node[i]:
        final_activate_node.append(i)
        if candidate_node[i]:
            final_candidate_node.append(i)

ans = False
temp_result = True

def traverse(cur):
    global temp_result
    visited[cur] = True
    for next in edge[cur]:
        if visited[next]:
            temp_result = False
            return
        traverse(next)
    return

for root in final_candidate_node:
    visited = [False for i in range(N + 1)]
    temp_result = True
    traverse(root)
    for node in final_activate_node:
        if not visited[node]:
            temp_result = False

    if temp_result:
        ans = True
        break

if ans:
    print(1)
else:
    print(0)