import copy

direct_print = ["↑","↖","←","↙","↓","↘","→","↗"]
BOARD_SIZE = 4
NO_PIECE = (0,0)
OUT_OF_GRID = (100,100)
dxs = [-1,-1,0,1,1,1,0,-1]
dys = [0,-1,-1,-1,0,1,1,1]
grid = []

for i in range(BOARD_SIZE):
    p1, d1, p2, d2, p3, d3, p4, d4 = map(int,input().split())
    grid.append([(p1,d1-1),(p2,d2-1),(p3,d3-1),(p4,d4-1)])

first_score = grid[0][0][0]
td = grid[0][0][1]
grid[0][0] = (-1,td)
ans = 0

#########################################################

def in_range(x,y):
    return 0<=x<BOARD_SIZE and 0<=y<BOARD_SIZE

def can_go(x,y):
    return in_range(x,y) and grid[x][y][0] != -1

def print_grid():
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            print(f"{grid[x][y][0]:2}",direct_print[grid[x][y][1]],end=' ')
        print()
    print()

def get_candidate():
    # 술래 위치를 찾습니다.
    candidate = []
    x, y = find_player(-1)
    td = grid[x][y][1]

    while in_range(x,y):
        if grid[x][y][0] != 0 and grid[x][y][0] != -1:
            candidate.append(grid[x][y][0])
        x, y = x + dxs[td], y + dys[td]
    return candidate

def select_best(candidate,score):
    if not candidate:
        global ans
        ans = max(ans,score)
        return

    # 만약 후보가 남아 있다면...
    for c in candidate:
        temp = copy.deepcopy(grid)

        # c를 잡는다
        tx, ty = find_player(-1)
        grid[tx][ty] = NO_PIECE
        cx, cy = find_player(c)
        cd = grid[cx][cy][1]
        grid[cx][cy] = (-1,cd)

        # 움직인다.
        move_all_pieces()

        # 새로운 후보를 구한다
        new_candidate = get_candidate()
        select_best(new_candidate,score+c)

        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                grid[i][j] = temp[i][j]
    return

def find_player(piece_num):
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if grid[x][y][0] == piece_num:
                return x, y
    return OUT_OF_GRID

def move_all_pieces():

    for c in range(1,17):
        x, y = find_player(c)
        if (x,y) == OUT_OF_GRID:
            continue
        d = grid[x][y][1]

        # 만약 아직 살아 있다면
        for i in range(8):
            di = (d+i) % 8
            dx, dy = dxs[di], dys[di]
            nx, ny = x + dx, y + dy
            if can_go(nx,ny):
                grid[x][y] = (c,di)
                switch(x,y,nx,ny)
                break

    return

def switch(x,y,nx,ny):
    temp = grid[x][y]
    grid[x][y] = grid[nx][ny]
    grid[nx][ny] = temp
    return

#########################################################

move_all_pieces()
candidate = get_candidate()
select_best(candidate,first_score)
print(ans)