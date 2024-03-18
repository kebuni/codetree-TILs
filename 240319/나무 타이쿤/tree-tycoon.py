dxs = [0,-1,-1,-1,0,1,1,1]
dys = [1,1,0,-1,-1,-1,0,1]

N, M = map(int,input().split())
grid = [list(map(int,input().split())) for i in range(N)]
delta = [[0 for i in range(N)] for j in range(N)]
nutrition_grid = [[0 for i in range(N)] for j in range(N)]
next_nutrition_grid = [[0 for i in range(N)] for j in range(N)]
nutrition_motion = []
for _ in range(M):
    d, p = map(int,input().split())
    nutrition_motion.append((d-1,p))

PADDING = N*10
nutrition_grid[N-1][0] = 1
nutrition_grid[N-1][1] = 1
nutrition_grid[N-2][0] = 1
nutrition_grid[N-2][1] = 1
###################################################

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def move_nutrition(d,p):
    clear_next_nutrition_grid()
    for x in range(N):
        for y in range(N):
            if nutrition_grid[x][y]:
                nx = (x + p * dxs[d] + PADDING) % N
                ny = (y + p * dys[d] + PADDING) % N
                next_nutrition_grid[nx][ny] = 1
    copy_nutrition_grid()
    return

def clear_next_nutrition_grid():
    for i in range(N):
        for j in range(N):
            next_nutrition_grid[i][j] = 0
    return

def copy_nutrition_grid():
    for i in range(N):
        for j in range(N):
            nutrition_grid[i][j] = next_nutrition_grid[i][j]
    return

def grow():
    for x in range(N):
        for y in range(N):
            if nutrition_grid[x][y]:
                grid[x][y] += 1
    for x in range(N):
        for y in range(N):
            if nutrition_grid[x][y]:
                grow = 0
                for i in [1,3,5,7]:
                    nx, ny = x + dxs[i], y + dys[i]
                    if in_range(nx,ny) and grid[nx][ny]:
                        grow += 1
                delta[x][y] = grow
                #nutrition_grid[x][y] += 1
    add_delta()
    return

def add_delta():
    for i in range(N):
        for j in range(N):
            grid[i][j] += delta[i][j]
            delta[i][j] = 0
    return

def buy_new_nutrition():
    for x in range(N):
        for y in range(N):
            if nutrition_grid[x][y]:
                nutrition_grid[x][y] = 0
            else:
                if grid[x][y] >= 2:
                    grid[x][y] -= 2
                    nutrition_grid[x][y] = 1
    return

def print_status():
    for i in range(N):
        for j in range(N):
            print(f'{grid[i][j]:2}',end=' ')
        print("",end='     ')
        for j in range(N):
            print(f'{nutrition_grid[i][j]:2}',end=' ')
        print()
    print()

###################################################

for i in range(M):
    #print("------------",i)
    d, p = nutrition_motion[i]
    move_nutrition(d,p)
    # print("after_move")
    # print_status()

    grow()
    # print("after_grow")
    # print_status()

    buy_new_nutrition()
    # print("after_new_nutrition")
    # print_status()

print(sum([grid[x][y] for x in range(N) for y in range(N)]))