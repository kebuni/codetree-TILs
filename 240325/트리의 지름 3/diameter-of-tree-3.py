import sys
sys.setrecursionlimit(100000)

# 변수 선언 및 입력:
n = int(input())
edges = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
dist = [0] * (n + 1)
max_dist = 0
last_node = 0
a, b, ans = 0, 0, 0

# n - 1개의 간선 정보를 입력받습니다.
for _ in range(n - 1):
    x, y, d = tuple(map(int, input().split()))
    edges[x].append((y, d))
    edges[y].append((x, d))


# 모든 노드의 정점을 탐색하는 DFS를 진행합니다.
def dfs(x, ignore_num):
    global max_dist, last_node
    
    for y, d in edges[x]:
        # 이미 방문한 정점이면 스킵합니다.
        if visited[y]: 
            continue

        visited[y] = True
        dist[y] = dist[x] + d

        # 현재 정점을 기준으로 가장 먼 노드를 찾습니다.
        # 단, ignore_num이면 무시합니다.
        if dist[y] > max_dist and y != ignore_num:
            max_dist = dist[y]
            last_node = y

        dfs(y, ignore_num)


# DFS를 통해 가장 먼 노드를 찾습니다. 이 노드를 a라 합니다.
visited[1] = True
dfs(1, -1)
a = last_node

# 다시 한번 먼 노드를 찾아줍니다. 이 위치를 b라 합니다.
for i in range(1, n + 1):
    visited[i] = False
    dist[i] = 0
max_dist = -1
visited[a] = True
dfs(a, -1)
b = last_node

# 이제 a에서 b를 제외한 노드 중 가장 먼 노드까지의 거리를 구합니다.
# 이후 답을 갱신합니다.
for i in range(1, n + 1):
    visited[i] = False
    dist[i] = 0
max_dist = -1
visited[a] = True
dfs(a, b)
ans = max(ans, max_dist)

# 이제 b에서 a를 제외한 노드 중 가장 먼 노드까지의 거리를 구합니다.
# 이후 답을 갱신합니다.
for i in range(1, n + 1):
    visited[i] = False
    dist[i] = 0
max_dist = -1
visited[b] = True
dfs(b, a)
ans = max(ans, max_dist)

print(ans)