from collections import deque

n, Q = map(int,input().split())
N = 2**n
grid = [list(map(int,input().split())) for i in range(N)]
delta = [[0 for i in range(N)] for j in range(N)]
visited = [[False for i in range(N)] for j in range(N)]
rotate_list = list(map(int,input().split()))

q = deque()
max_size = 0
cur_size = 0

dxs = [-1,0,1,0]
dys = [0,1,0,-1]

#######################################################

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def can_go(x,y):
    return in_range(x,y) and not visited[x][y] and grid[x][y] > 0

def bfs(x,y):
    global max_size, cur_size
    cur_size = 0
    push(x,y)
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                push(nx, ny)

    max_size = max(max_size, cur_size)
    return

def push(x,y):
    global cur_size
    visited[x][y] = True
    cur_size += 1
    q.append((x,y))
    return

def rotate(level):
    if level == 0:
        return

    k = 2**level

    for i in range(2**(n-level)):
        for j in range(2**(n-level)):
            #print(i*k,j*k)
            rotate_one(i*k,j*k,level)

    return

def rotate_one(x,y,l):
    k = 2**(l-1)
    # temp 저장
    temp = [[0 for i in range(k)] for j in range(k)]
    for i in range(k):
        for j in range(k):
            temp[i][j] = grid[x+i][y+j]
    # 왼쪽 아래에서 왼쪽 위로 옮기기
    for i in range(k):
        for j in range(k):
            grid[x+i][y+j] = grid[x+k+i][y+j]
    # 오른쪽 아래에서 왼쪽 아래로 옮기기
    for i in range(k):
        for j in range(k):
            grid[x+k+i][y+j] = grid[x+k+i][y+k+j]
    # 오른쪽 위에서 오른쪽 아래로 옮기기
    for i in range(k):
        for j in range(k):
            grid[x+k+i][y+k+j] = grid[x+i][y+k+j]
    # 오른쪽 위에 temp 넣기
    for i in range(k):
        for j in range(k):
            grid[x+i][y+k+j] = temp[i][j]

    return

def melt():
    for x in range(N):
        for y in range(N):
            if grid[x][y]:
                if get_neighboring_ice_num(x,y) < 3:
                    delta[x][y] = -1
    add_and_clear_delta()
    return

def get_neighboring_ice_num(x,y):
    result = 0
    for dx, dy in zip(dxs,dys):
        nx, ny = x + dx, y + dy
        if in_range(nx,ny) and grid[nx][ny]:
            result += 1
    return result

def add_and_clear_delta():
    for x in range(N):
        for y in range(N):
            grid[x][y] += delta[x][y]
            delta[x][y] = 0
    return

def get_glacier_sum():
    return sum([grid[x][y] for x in range(N) for y in range(N)])

def get_max_size():
    for x in range(N):
        for y in range(N):
            if grid[x][y] and not visited[x][y]:
                bfs(x,y)
    return

def print_grid():
    for x in range(N):
        for y in range(N):
            print(f'{grid[x][y]:2}',end=' ')
        print()
    print()

#######################################################

for level in rotate_list:
    rotate(level)
    #print_grid()
    melt()
    #print_grid()

print(get_glacier_sum())
get_max_size()
print(max_size)