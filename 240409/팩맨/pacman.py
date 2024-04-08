dxs = [-1,-1,0,1,1,1,0,-1]
dys = [0,-1,-1,-1,0,1,1,1]
d_to_arrow = ['↑', '↖', '←', '↙', '↓', '↘', '→', '↗']

M, T = map(int,input().split())
PX, PY = map(lambda x:int(x)-1,input().split())
grid = [[[0 for i in range(8)] for j in range(4)] for k in range(4)]
next_grid = [[[0 for i in range(8)] for j in range(4)] for k in range(4)]
egg = [[[0 for i in range(8)] for j in range(4)] for k in range(4)]
body = [[0 for i in range(4)] for j in range(4)]
for i in range(M):
    r, c, d = map(int,input().split())
    grid[r-1][c-1][d-1] += 1

#######################################################

def in_range(x,y):
    return 0<=x<4 and 0<=y<4

def can_go(x,y):
    return in_range(x,y) and body[x][y] == 0 and (x,y) != (PX,PY)

def copy_egg():
    for x in range(4):
        for y in range(4):
            for i in range(8):
                egg[x][y][i] = grid[x][y][i]
    return

def move_all_monster():
    clear_next_grid()
    for x in range(4):
        for y in range(4):
            for d in range(8):
                if grid[x][y][d]:
                    nx, ny, nd = move_one(x,y,d)
                    next_grid[nx][ny][nd] += grid[x][y][d]
    copy_next_grid()
    return

def move_one(x,y,d):
    for i in range(8):
        nd = (d+i) % 8
        nx, ny = x + dxs[nd], y + dys[nd]
        if can_go(nx,ny):
            return nx, ny, nd
    return x, y, d

def clear_next_grid():
    for x in range(4):
        for y in range(4):
            for i in range(8):
                next_grid[x][y][i] = 0
    return

def copy_next_grid():
    for x in range(4):
        for y in range(4):
            for i in range(8):
                grid[x][y][i] = next_grid[x][y][i]
    return

def move_pacman():
    global PX, PY
    # 팩맨의 경로를 정합니다.
    path = get_path()
    # 팩맨이 경로를 따라 이동하면서 시체를 만듭니다.
    for x, y in path:
        for d in range(8):
            if grid[x][y][d]:
                grid[x][y][d] = 0
                body[x][y] = 3
    # 팩맨의 위치를 업데이트합니다.
    PX, PY = path[-1]
    return

def get_path():
    max_kill = -1
    best_path = []
    temp_path = []
    for d1 in [0,2,4,6]:
        x1, y1 = PX + dxs[d1], PY + dys[d1]
        if not in_range(x1,y1):
            continue
        temp_path.append((x1,y1))
        for d2 in [0,2,4,6]:
            x2, y2 = x1 + dxs[d2], y1 + dys[d2]
            if not in_range(x2, y2):
                continue
            temp_path.append((x2,y2))
            for d3 in [0,2,4,6]:
                x3, y3 = x2 + dxs[d3], y2 + dys[d3]
                if not in_range(x3, y3):
                    continue
                temp_path.append((x3,y3))

                # 이제 3칸 이동했으니 잡은 몬스터수 확인
                temp_path_set = set(temp_path[:])
                temp_kill = 0
                for x, y in temp_path_set:
                    temp_kill += sum(grid[x][y])
                if temp_kill > max_kill:
                    max_kill = temp_kill
                    best_path = temp_path[:]

                temp_path.pop()
            temp_path.pop()
        temp_path.pop()

    # print("best path:",best_path)
    return best_path

def remove_body():
    for x in range(4):
        for y in range(4):
            if body[x][y]:
                body[x][y] -= 1
    return

def paste_egg():
    for x in range(4):
        for y in range(4):
            for i in range(8):
                grid[x][y][i] += egg[x][y][i]
                egg[x][y][i] = 0
    return

def print_ans():
    ans = 0
    for x in range(4):
        for y in range(4):
            ans += sum(grid[x][y])
    print(ans)
    return

def print_grid():
    for x in range(4):
        for y in range(4):
            for i in range(8):
                print(d_to_arrow[i],end='')
                print(grid[x][y][i],end='')
            print(" ",end='')
        print()
    for x in range(4):
        for y in range(4):
            print(sum(grid[x][y]),end=' ')
        print()
    print()
    return

def print_body():
    for x in range(4):
        for y in range(4):
            print(body[x][y],end=' ')
        print()
    print()
    return

#######################################################

for i in range(T):
    # print("--------------------------------------")
    copy_egg()

    move_all_monster()
    # print("after move all monster")
    # print_grid()

    move_pacman()
    # print("after move pacman")
    # print_grid()
    # print_body()
    # print("PX,PY:",PX,PY)

    remove_body()
    # print("after remove body")
    # print_body()

    paste_egg()
    # print("after paste egg")
    # print_grid()

print_ans()