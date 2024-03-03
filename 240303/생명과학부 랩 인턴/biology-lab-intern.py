NO_FUN = (0,0,0)
dxs = [-1,1,0,0]
dys = [0,0,1,-1]

N, M, K = map(int,input().split())

grid = [[ NO_FUN for i in range(M)] for j in range(N)]
next_grid = [[ NO_FUN for i in range(M)] for j in range(N)]
ans = 0

for _ in range(K):
    x, y, s, d, b = map(int,input().split())
    grid[x-1][y-1] = (b,s,d-1)

#####################################

def print_grid():
    for i in range(N):
        for j in range(M):
            print(grid[i][j],end=' ')
        print()
    print()

def clear_next_grid():
    for i in range(N):
        for j in range(M):
            next_grid[i][j] = NO_FUN
    return

def in_range(x,y):
    return 0<=x<N and 0<=y<M

def find_fun(intern_y):
    global ans
    for x in range(N):
        if grid[x][intern_y] != NO_FUN:
            ans += grid[x][intern_y][0]
            grid[x][intern_y] = NO_FUN
            return
            #return True
    #return False

def move_fun():
    for i in range(N):
        for j in range(M):
            if grid[i][j] != NO_FUN:

                # 현재 보고 있는 곰팡이를 넣자
                x,y = i, j
                size, speed, d = grid[i][j]
                for t in range(speed):
                    nx, ny = x + dxs[d], y + dys[d]
                    if in_range(nx,ny):
                        x, y = nx, ny
                    else:
                        d = d^1
                        x, y = x + dxs[d], y + dys[d]

                # 이동이 다 끝났으면 next에 넣어주는데, 잡아먹는거 고려
                if next_grid[x][y] != NO_FUN:
                    cur_size = next_grid[x][y][0]
                    if size > cur_size:
                        next_grid[x][y] = (size,speed,d)
                    else:
                        continue
                else:
                    next_grid[x][y] = (size,speed,d)

    return

def copy_grid():
    for i in range(N):
        for j in range(M):
            grid[i][j] = next_grid[i][j]

#####################################

for intern_y in range(M):
    # 현재 열에서 곰팡이 찾아서 삭제. 만약 있으면 이동시키고 없으면 다음 열

    find_fun(intern_y)
    clear_next_grid()
    move_fun()
    copy_grid()

print(ans)