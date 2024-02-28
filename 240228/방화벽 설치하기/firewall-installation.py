import copy
from collections import deque

N, M = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(N)]
cur_grid = [[0 for i in range(M)] for j in range(N)]
candidate = []
fire_list = []
selected = []
ans = 0
q = deque()
dxs = [-1,0,1,0]
dys = [0,1,0,-1]

for i in range(N):
    for j in range(M):
        if grid[i][j] == 0:
            candidate.append((i,j))
        elif grid[i][j] == 2:
            fire_list.append((i,j))

##################################

def find_min(n,m):
    if m == 3:
        global cur_grid

        copy_grid()
        #print(selected)

        for x, y in selected:
            # 방화벽 세우고 불내기
            cur_grid[x][y] = 1
        bfs()
        #print_cur_grid()
        update_ans()
        return

    # 아직 3개를 못채웠는데 다 됐으면
    if n == len(candidate):
        return

    # 아직 고르는게 끝나지 않았다면

    selected.append(candidate[n])
    find_min(n+1,m+1)
    selected.pop()
    find_min(n + 1, m)

    return

def bfs():
    q.clear()
    for x, y in fire_list:
        q.append((x,y))

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs,dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                cur_grid[nx][ny] = 2
                q.append((nx,ny))
    return

def in_range(x,y):
    return 0<=x<N and 0<=y<M

def can_go(x,y):
    return in_range(x,y) and not cur_grid[x][y]

def copy_grid():
    global cur_grid
    for i in range(N):
        for j in range(M):
            cur_grid[i][j] = grid[i][j]

def update_ans():
    global ans
    sum = 0
    for i in range(N):
        for j in range(M):
            if cur_grid[i][j] == 0:
                sum += 1
    ans = max(ans,sum)
    return

def print_cur_grid():
    for i in range(N):
        for j in range(M):
            print(cur_grid[i][j], end= ' ')
        print()
    print()

##################################

find_min(0,0)
print(ans)