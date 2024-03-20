import sys
INF = sys.maxsize

N, K = map(int,input().split())
grid = [[0 for i in range(N)] for j in range(N-1)]
grid.append(list(map(int,input().split())))
temp = [[0 for i in range(N)] for j in range(N)]

################################################
def print_grid():
    for i in range(N):
        for j in range(N):
            print(f'{grid[i][j]:2}',end=' ')
        print()
    print()
    return

def check_end():
    max_flour = -INF
    min_flour = INF
    for y in range(N):
        max_flour = max(max_flour,grid[N-1][y])
        min_flour = min(min_flour,grid[N-1][y])
    if max_flour - min_flour <= K:
        return True
    else:
        return False

def add_flour():
    min_flour = INF
    for y in range(N):
        min_flour = min(min_flour,grid[N-1][y])
    for y in range(N):
        if grid[N-1][y] == min_flour:
            grid[N-1][y] += 1
    return

def roll_dough():
    m2 = 2
    l2 = 3
    pivot = 1
    while N - pivot >= l2 // 2:
        m = m2 // 2
        l = l2 // 2

        for i in range(m):
            for j in range(l):
                grid[N-2-i][pivot+j] = grid[N-1-j][pivot-1-i]
                grid[N - 1 - j][pivot - 1 - i] = 0

        pivot += l
        m2 += 1
        l2 += 1
    return

def press_dough():
    dxs = [1,0]
    dys = [0,1]

    for x in range(N):
        for y in range(N):
            if grid[x][y]:
                for dx, dy in zip(dxs,dys):
                    nx, ny = x + dx, y + dy
                    if can_go(nx,ny):
                        press_one(x,y,nx,ny)

    add_and_clear_temp()

    idx = 0
    for y in range(N):
        for x in range(N-1,-1,-1):
            if grid[x][y]:
                temp[N-1][idx] = grid[x][y]
                idx += 1

    copy_and_clear_temp()

    return

def add_and_clear_temp():
    for i in range(N):
        for j in range(N):
            grid[i][j] += temp[i][j]
            temp[i][j] = 0
    return

def copy_and_clear_temp():
    for i in range(N):
        for j in range(N):
            grid[i][j] = temp[i][j]
            temp[i][j] = 0
    return

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def can_go(x,y):
    return in_range(x,y) and grid[x][y]

def press_one(x,y,nx,ny):
    flour1 = grid[x][y]
    flour2 = grid[nx][ny]
    diff = abs(flour1-flour2)
    if flour1 > flour2:
        temp[x][y] -= diff // 5
        temp[nx][ny] += diff // 5
    elif flour1 < flour2:
        temp[x][y] += diff // 5
        temp[nx][ny] -= diff // 5
    return

def fold_dough():
    for i in range(N//4):
        grid[N-2][N-1-i] = grid[N-1][i]
    for i in range(N//4):
        grid[N-3][N//4*3+i] = grid[N-1][i+N//4]
    for i in range(N//4):
        grid[N-4][N-1-i] = grid[N-1][i+N//4*2]
    for i in range(N//4*3):
        grid[N-1][i] = 0
    return

################################################

ans = 0

while not check_end():
    add_flour()
    # print("after add")
    # print_grid()

    roll_dough()
    # print("after roll")
    # print_grid()

    press_dough()
    # print("after press")
    # print_grid()

    fold_dough()
    # print("after fold")
    # print_grid()

    press_dough()
    # print("after press")
    # print_grid()

    ans += 1

print(ans)