import sys
sys.setrecursionlimit(2000)

# 변수 선언 및 입력 :
n = int(input())
edge = [[] for _ in range(n)]
removed = [
    [False] * n
    for _ in range(n)
]
edge_x = [0] * n
edge_y = [0] * n
edge_dist = [0] * n

visited = [False] * n
dist_node = [0] * n
dist = [0] * n
max_dist = 0
last_node = 0
ans = 0

# n - 1개의 간선 정보를 입력받습니다.
for i in range(n - 1):
    x, y, d = tuple(map(int, input().split()))
    edge_x[i] = x
    edge_y[i] = y
    edge_dist[i] = d

    edge[x].append((y, d))
    edge[y].append((x, d))


# 모든 노드의 정점을 탐색하는 DFS를 진행합니다.
def dfs(x):
    global max_dist, last_node

    for y, d in edge[x]:
        # 지워진 간선이면 스킵합니다.
        if removed[x][y]: 
            continue

        # 이미 방문한 정점이면 스킵합니다.
        if visited[y]: 
            continue

        visited[y] = True
        dist[y] = dist[x] + d

        # 현재 정점을 기준으로 가장 먼 노드를 찾습니다.
        if dist[y] > max_dist:
            max_dist = dist[y]
            last_node = y

        dfs(y)


def get_tree_diameter(x):
    global max_dist, last_node
    
    # 전역변수들을 초기화합니다.
    for i in range(n):
        visited[i] = False
        dist[i] = 0
    
    max_dist = 0
    last_node = x

    # dfs를 통해 가장 멀리 있는 정점을 찾습니다.
    visited[x] = True
    dfs(x)

    # 전역변수들을 초기화합니다.
    for i in range(n):
        visited[i] = False
        dist[i] = 0
    
    max_dist = 0

    # dfs를 통해 가장 멀리 있는 정점에서 트리의 지름을 찾습니다. 
    visited[last_node] = True   
    dfs(last_node)

    return max_dist


# n - 1개의 간선을 하나씩 지우고 생긴 두 트리 각각의 지름을 찾습니다.
for i in range(n - 1):
    removed[edge_x[i]][edge_y[i]] = True
    removed[edge_y[i]][edge_x[i]] = True

    # i번 간선을 지우고 새로 그었을 때, 만들어질 수 있는 최대 지름을 찾습니다.
    # i번 간선을 지운 뒤 생긴 두 트리에서의 지름을 새로 연결할 때 최대 지름이 됩니다.
    max_diameter = edge_dist[i] + get_tree_diameter(edge_x[i]) + get_tree_diameter(edge_y[i])
    ans = max(ans, max_diameter)

    removed[edge_x[i]][edge_y[i]] = False
    removed[edge_y[i]][edge_x[i]] = False

# 만들 수 있는 트리의 가장 큰 지름을 출력합니다.
print(ans)