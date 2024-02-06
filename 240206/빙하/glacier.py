from collections import deque
grid = []
next_grid = []
visited = []
dxs = [-1,0,1,0]
dys = [0,1,0,-1]
q = deque()
glacier_size = 0
elapsed_time = 0

####################

def get_glacier_size():
    sum = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                sum += 1
    return sum

def in_range(x,y):
    return 0<=x<N and 0<=y<M

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y]:
        return False
    if grid[x][y] == 1:
        return False
    return True

def push(x,y):
    global q,visited
    visited[x][y] = 1
    q.append((x,y))
    return

def bfs():
    global q
    while q:
        x,y = q.popleft()
        for dx, dy in zip(dxs,dys):
            nx = x + dx
            ny = y + dy
            if can_go(nx,ny):
                push(nx,ny)
    return

def melt():
    global grid
    for x in range(N):
        for y in range(M):
            # 빙하라면,
            if grid[x][y] == 1:
                for dx, dy in zip(dxs, dys):
                    nx = x + dx
                    ny = y + dy
                    if visited[nx][ny]:
                        grid[x][y] = 0
                        break
    return

def clear_visited():
    global visited
    for x in range(N):
        for y in range(M):
            visited[x][y] = 0

def print_grid():
    for x in range(N):
        for y in range(M):
            print(grid[x][y],end=' ')
        print()
    print()

####################

N, M = map(int,input().split())
for _ in range(N):
    grid.append(list(map(int,input().split())))
    next_grid.append([0 for i in range(M)])
    visited.append([0 for i in range(M)])

glacier_size = get_glacier_size()
#print_grid()
while True:

    clear_visited()
    push(0,0)
    bfs()
    melt()

    #print_grid()

    elapsed_time += 1

    temp = get_glacier_size()
    if not temp:
        break

    glacier_size = temp

print(elapsed_time, glacier_size)