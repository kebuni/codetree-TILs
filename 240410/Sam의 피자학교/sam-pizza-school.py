N, K = map(int,input().split())
grid = [[0 for i in range(N)] for j in range(N-1)]
grid.append(list(map(int,input().split())))

DOUGH = N-1
##############################################

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def print_grid():
    for x in range(N):
        for y in range(N):
            print(f'{grid[x][y]:2}',end=' ')
        print()
    print()
    return

def add_flour():
    min_flour = min(grid[DOUGH])
    for y in range(N):
        if grid[DOUGH][y] == min_flour:
            grid[DOUGH][y] += 1
    return

def roll_dough():
    p = 1
    l = 1
    _l = 3
    while p+l-1 <= N-1:

        # print("p,l", p, l)
        for y in range(p):
            for x in range(N-1,-1,-1):
                if grid[x][y]:
                    grid[N-1+(y-p)][p-(x-(N-1))] = grid[x][y]
                    grid[x][y] = 0

        # print_grid()

        p += l
        _l += 1
        l = _l // 2

    return

def press_dough():

    dxs = [1,0]
    dys = [0,1]

    delta = [[0 for i in range(N)] for j in range(N)]
    for x in range(N):
        for y in range(N):
            if grid[x][y]:
                for dx, dy in zip(dxs,dys):
                    nx, ny = x + dx, y + dy
                    if in_range(nx,ny) and grid[nx][ny]:
                        diff = abs(grid[x][y] - grid[nx][ny]) // 5
                        if grid[x][y] > grid[nx][ny]:
                            delta[x][y] -= diff
                            delta[nx][ny] += diff
                        else:
                            delta[x][y] += diff
                            delta[nx][ny] -= diff

    for x in range(N):
        for y in range(N):
            grid[x][y] += delta[x][y]

    # 도우 펴기
    temp_dough = []
    for y in range(N):
        for x in range(N-1,-1,-1):
            if grid[x][y]:
                temp_dough.append(grid[x][y])

    for x in range(N):
        for y in range(N):
            grid[x][y] = 0

    for i, elem in enumerate(temp_dough):
        grid[DOUGH][i] = elem

    return

def fold_dough():
    Q = N//4
    temp_dough = grid[DOUGH][:]
    for y in range(N):
        grid[DOUGH][y] = 0

    for i in range(Q):
        grid[DOUGH-1][N-1-i] = temp_dough[i]

    for i in range(Q):
        grid[DOUGH-2][3*Q+i] = temp_dough[Q+i]

    for i in range(Q):
        grid[DOUGH-3][N-1-i] = temp_dough[2*Q+i]

    for i in range(Q):
        grid[DOUGH][3*Q+i] = temp_dough[3*Q+i]

    return

def check_end():
    return max(grid[DOUGH]) - min(grid[DOUGH]) <= K

##############################################
ans = 0
while not check_end():
    # print("--------------------",ans)

    add_flour()
    # print("after add flour")
    # print_grid()

    roll_dough()
    # print("after roll dough")
    # print_grid()

    press_dough()
    # print("after press dough")
    # print_grid()

    fold_dough()
    # print("after fold dough")
    # print_grid()

    press_dough()
    # print("after press dough")
    # print_grid()

    ans += 1

print(ans)