dxs = [-1,0,1,0]
dys = [0,1,0,-1]
dxs_diagonal = [-1,1,1,-1]
dys_diagonal = [1,1,-1,-1]

N, M, K, C = map(int,input().split())
grid = [list(map(int,input().split())) for i in range(N)]
temp = [[0 for i in range(N)] for j in range(N)]
chemical = [[0 for i in range(N)] for j in range(N)]

####################################################

def print_grid():
    for x in range(N):
        for y in range(N):
            print(f'{grid[x][y]:2}',end=' ')
        print()
    print()
    return

def print_chemical():
    for x in range(N):
        for y in range(N):
            print(f'{chemical[x][y]:2}',end=' ')
        print()
    print()
    return

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def can_go(x,y):
    return in_range(x,y) and grid[x][y] == 0 and not chemical[x][y]

def clear_temp():
    for x in range(N):
        for y in range(N):
            temp[x][y] = 0
    return

def add_temp():
    for x in range(N):
        for y in range(N):
            grid[x][y] += temp[x][y]
    return

def grow_tree():
    clear_temp()
    for x in range(N):
        for y in range(N):
            if grid[x][y] > 0:
                for dx, dy in zip(dxs,dys):
                    nx, ny = x + dx, y + dy
                    if in_range(nx,ny) and grid[nx][ny] > 0:
                        temp[x][y] += 1
    add_temp()
    return

def spread_tree():
    clear_temp()
    for x in range(N):
        for y in range(N):
            if grid[x][y] > 0:
                cur = grid[x][y]
                spread_num = 0
                spread_pos = []
                for dx, dy in zip(dxs,dys):
                    nx, ny = x + dx, y + dy
                    if can_go(nx,ny):
                        spread_pos.append((nx,ny))
                        spread_num += 1
                for sx, sy in spread_pos:
                    temp[sx][sy] += cur // spread_num
    add_temp()
    return

def kill_tree():
    max_kill_num = -1
    result_pos = []

    for x in range(N):
        for y in range(N):
            if grid[x][y] > 0:
                temp_kill_num, temp_pos = kill_tree_one(x,y)
                if temp_kill_num > max_kill_num:
                    max_kill_num = temp_kill_num
                    result_pos = temp_pos[:]

    global killed_tree
    killed_tree += max_kill_num

    for x, y in result_pos:
        grid[x][y] = 0
        chemical[x][y] = C + 1

    return

def kill_tree_one(init_x,init_y):
    temp_pos = [(init_x,init_y)]
    temp_kill_num = grid[init_x][init_y]

    for dx, dy in zip(dxs_diagonal, dys_diagonal):
        x, y = init_x, init_y
        for i in range(K):
            x, y = x + dx, y + dy
            if not in_range(x,y):
                break
            if grid[x - dx][y - dy] == 0 or grid[x - dx][y - dy] == -1:
                break
            # 여기 까지 왔으면 격자 내고, 이전칸이 빈칸도 벽도 아님 -> 현재 칸에 대해 진행
            temp_pos.append((x,y))
            if grid[x][y] != -1:
                temp_kill_num += grid[x][y]

    return temp_kill_num, temp_pos

def decrease():
    for x in range(N):
        for y in range(N):
            if chemical[x][y]:
                chemical[x][y] -= 1
    return

####################################################
killed_tree = 0
for i in range(M):
    grow_tree()
    # print("after grow")
    # print_grid()

    spread_tree()
    # print("after spread")
    # print_grid()

    kill_tree()
    # print("after kill")
    # print_grid()
    # print_chemical()

    decrease()
    # print("after decrease")
    # print_chemical()

print(killed_tree)