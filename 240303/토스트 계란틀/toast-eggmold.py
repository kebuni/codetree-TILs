from collections import deque

N, L, R = map(int,input().split())

grid = [list(map(int,input().split())) for i in range(N)]
next_grid = [[0 for i in range(N)] for j in range(N)]
visited = [[False for i in range(N)] for j in range(N)]
q = deque()
ans = 0

dxs = [-1,0,1,0]
dys = [0,1,0,-1]
cur_size = 0
cur_sum = 0
cur_list = []

############################################

def clear_next_grid():
    for i in range(N):
        for j in range(N):
            next_grid[i][j] = 0
            visited[i][j] = False

def copy_grid():
    for i in range(N):
        for j in range(N):
            grid[i][j] = next_grid[i][j]

def print_grid():
    for i in range(N):
        for j in range(N):
            print(grid[i][j],end=' ')
        print()
    print()

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def can_go(x,y,nx,ny):
    return in_range(nx,ny) and not visited[nx][ny] \
        and L <= abs(grid[nx][ny] - grid[x][y]) <= R

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs,dys):
            nx, ny = x + dx, y + dy
            if can_go(x,y,nx,ny):
                push(nx,ny)
    return

def push(x,y):
    global q, visited, cur_size, cur_sum
    visited[x][y] = True
    cur_size += 1
    cur_sum += grid[x][y]
    cur_list.append((x,y))
    q.append((x,y))
    return

############################################

keep = True

while keep:
    keep = False
    # 새로운 스텝이므로 clear해줍니다.
    clear_next_grid()

    # 모든 x,y에 대하여,
    for x in range(N):
        for y in range(N):
            # 만약 (x,y)가 처음 보는 곳이면 탐색을 시작합니다.
            if not visited[x][y]:
                cur_sum = 0
                cur_size = 0
                cur_list = []
                push(x,y)
                bfs()
                # 이제 계란틀 분리가 끝났습니다. 만약 두개 이상이면 다음 단계도 봅니다.
                if cur_size > 1:
                    keep = True
                for cx, cy in cur_list:
                    grid[cx][cy] = cur_sum // cur_size

    if keep: #keep 이 참이라는 것은 계란 이동이 일어났다는 뜻입니다.
        ans += 1

    #print_grid()

print(ans)