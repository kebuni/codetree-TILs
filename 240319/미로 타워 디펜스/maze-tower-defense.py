N, M = map(int,input().split())
grid = [list(map(int,input().split())) for i in range(N)]
next_grid = [[0 for i in range(N)] for j in range(N)]
attack_list = [tuple(map(int,input().split())) for i in range(M)]
score = 0
Tx, Ty = N//2, N//2

dxs = [1,0,-1,0]
dys = [0,1,0,-1]

idx_to_coord = {}

dist_list = [1]
for i in range(2, N):
    dist_list.append(i)
    dist_list.append(i)
dist_list.append(N)

###################################################

def init_dict():
    idx = 0
    x, y = Tx, Ty-1
    d = 0
    for dist in dist_list:
        for i in range(dist):
            idx_to_coord[idx] = (x,y)
            x, y = x + dxs[d], y + dys[d]
            idx += 1
        d = (d + 1) % 4
    return

def copy_and_clear_next_grid():
    for x in range(N):
        for y in range(N):
            grid[x][y] = next_grid[x][y]
            next_grid[x][y] = 0
    return

def attack(d,p):
    global score
    attack_direction_x = [0, 1, 0, -1]
    attack_direction_y = [1, 0, -1, 0]
    x, y = Tx, Ty
    for i in range(p):
        x = x + attack_direction_x[d]
        y = y + attack_direction_y[d]
        score += grid[x][y]
        grid[x][y] = 0
    return

def fill():
    idx = 0
    for i in range(N*N-1):
        x, y = idx_to_coord[i]
        if grid[x][y]:
            nx, ny = idx_to_coord[idx]
            next_grid[nx][ny] = grid[x][y]
            idx += 1
    copy_and_clear_next_grid()
    return

def delete():
    global score
    keep = False
    prev = grid[N // 2][N // 2 - 1]
    temp = [(N//2,N//2-1)]

    if prev == 0:
        return keep

    for i in range(1,N*N-1):
        x, y = idx_to_coord[i]
        cur = grid[x][y]
        if prev == cur:
            temp.append((x,y))
        else:
            if len(temp) >= 4:
                keep = True
                score += len(temp)*prev
                for del_x, del_y in temp:
                    grid[del_x][del_y] = 0
            prev = cur
            temp = [(x,y)]

    return keep

def rearrange():
    temp = []
    prev = grid[N//2][N//2-1]
    combo = 1

    if prev == 0:
        clear_grid()
        return

    for i in range(1,N*N-1):
        x, y = idx_to_coord[i]
        cur = grid[x][y]
        if cur == 0:
            temp.append(combo)
            temp.append(prev)
            break
        if cur == prev:
            combo += 1
        else:
            temp.append(combo)
            temp.append(prev)
            prev = cur
            combo = 1

    temp = temp[:N*N-1]
    idx = 0
    for elem in temp:
        x, y = idx_to_coord[idx]
        next_grid[x][y] = elem
        idx += 1
    copy_and_clear_next_grid()

    return

def print_grid():
    for x in range(N):
        for y in range(N):
            print(f'{grid[x][y]:3}',end=' ')
        print()
    print()

def clear_grid():
    for x in range(N):
        for y in range(N):
            grid[x][y] = 0
    return

###################################################

init_dict()

for i in range(M):
    d, p = attack_list[i]
    attack(d,p)
    # print("after attack")
    # print_grid()
    fill()
    # print("after fill")
    # print_grid()
    while delete():
        # print("delted!")
        # print_grid()
        fill()
        # print("after fill")
        # print_grid()
    rearrange()
    # print("after rearrange")
    # print_grid()

print(score)