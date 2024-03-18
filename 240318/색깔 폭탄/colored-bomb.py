from collections import deque

RED = 0
ROCK = -1
BLANK = -2

N, M = map(int,input().split())
grid = [list(map(int,input().split())) for i in range(N)]
next_grid = [[BLANK for i in range(N)] for j in range(N)]
visited = [[False for i in range(N)] for j in range(N)]

dxs = [-1,0,1,0]
dys = [0,1,0,-1]
q = deque()
selected_bombs = []
temp_bombs_list = []

cur_size = 0
cur_red_size = 0
############################################

def copy_grid():
    for i in range(N):
        for j in range(N):
            grid[i][j] = next_grid[i][j]
    return

def clear_next_grid():
    for i in range(N):
        for j in range(N):
            next_grid[i][j] = BLANK
    return

def clear_visited():
    for i in range(N):
        for j in range(N):
            visited[i][j] = False
    return

def clear_visited_only_red():
    for i in range(N):
        for j in range(N):
            if grid[i][j] == RED:
                visited[i][j] = False
    return

def print_grid():
    for i in range(N):
        for j in range(N):
            print(f'{grid[i][j]:2}',end=' ')
        print()
    print()

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def can_go(x,y,color):
    return in_range(x,y) and not visited[x][y] and (grid[x][y] == color or grid[x][y] == RED)

def select_bombs():
    global selected_bombs
    clear_visited()
    best = (-1,-1,-1,-1)
    for x in range(N):
        for y in range(N):
            if grid[x][y] > 0 and not visited[x][y]:
                temp_bombs = get_bomb_size(x,y)
                if best < temp_bombs:
                    best = temp_bombs
                    selected_bombs = temp_bombs_list[:]

    total_size, _, _, _ = best
    if total_size > 1:
        return True
    else:
        return False

def get_bomb_size(x,y):
    global cur_size, cur_red_size
    #print("now find the size of bombs start from" ,x,y)
    temp_bombs_list.clear()
    cur_size, cur_red_size = 0, 0
    max_row, min_col = x, y
    cur = grid[x][y]
    clear_visited_only_red()
    push(x,y)
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs,dys):
            nx, ny = x + dx, y + dy
            if can_go(nx,ny,cur):
                if grid[nx][ny] != RED:
                    max_row = max(max_row,nx)
                    min_col = min(min_col,ny)
                push(nx,ny)

    return (cur_size, -cur_red_size, max_row, -min_col)

def push(x,y):
    global cur_size, cur_red_size
    visited[x][y] = True
    cur_size += 1
    if grid[x][y] == RED:
        cur_red_size += 1
    temp_bombs_list.append((x,y))
    q.append((x,y))
    return

def remove_bombs():
    global score
    for x,y in selected_bombs:
        grid[x][y] = BLANK
    score += len(selected_bombs)**2
    return

def fall():
    clear_next_grid()
    for y in range(N):
        floor = N-1
        for x in range(N-1,-1,-1):
            if grid[x][y] == ROCK:
                next_grid[x][y] = ROCK
                floor = x-1
            elif grid[x][y] >= 0:
                next_grid[floor][y] = grid[x][y]
                floor -= 1
    copy_grid()
    return

def rotate():
    clear_next_grid()
    for i in range(N):
        for j in range(N):
            next_grid[N-1-j][i] = grid[i][j]
    copy_grid()
    return

############################################

score = 0

while True:
    # print('------------------')
    keep = select_bombs()
    # print(selected_bombs)
    if not keep:
        break

    remove_bombs()
    # print("after remove")
    # print_grid()

    fall()
    # print("after fall")
    # print_grid()

    rotate()
    # print("after rotate")
    # print_grid()

    fall()
    # print("after fall")
    # print_grid()

print(score)