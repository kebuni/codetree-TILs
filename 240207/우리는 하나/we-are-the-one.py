from collections import deque
grid = []
visited = []
city_cluster = []
q = deque()
dxs = [-1,0,1,0]
dys = [0,1,0,-1]
cur_dist = 0
ans = 0

##############################

def push(x,y):
    global cur_dist, visited, q
    visited[x][y] = 1
    cur_dist += 1
    q.append((x,y))
    return

def bfs():
    global q
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs,dys):
            nx = x + dx
            ny = y + dy
            #print(x,y,nx,ny)
            if can_go(x,y,nx,ny):
                #print("can go!")
                push(nx,ny)
    return

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def can_go(x,y,nx,ny):
    return in_range(nx,ny) and not visited[nx][ny] \
    and U <= abs(grid[nx][ny] - grid[x][y]) <= D

def clear_visited():
    global visited
    for i in range(N):
        for j in range(N):
            visited[i][j] = 0

##############################

N, K, U, D = map(int, input().split())
for _ in range(N):
    grid.append(list(map(int,input().split())))
    visited.append([0 for i in range(N)])

for x in range(N):
    for y in range(N):
        # 새로운 도시 클러스터를 찾았다면,
        if not visited[x][y]:
            cur_dist = 0
            push(x,y)
            bfs()
            city_cluster.append(cur_dist)

city_cluster.sort(reverse=True)
#print(city_cluster)
print(sum(city_cluster[:K]))