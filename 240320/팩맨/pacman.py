dxs = [-1,-1,0,1,1,1,0,-1]
dys = [0,-1,-1,-1,0,1,1,1]
d_to_arrow = ['↑', '↖', '←', '↙', '↓', '↘', '→', '↗']

N = 4

grid = [[[] for i in range(N)] for j in range(N)]
duplicate_grid = [[[] for i in range(N)] for j in range(N)]
next_grid = [[[] for i in range(N)] for j in range(N)]
dead_grid = [[[] for i in range(N)] for j in range(N)]

best_move = []
best_kill = -1
selected_move = []

M, T = map(int,input().split())
Px, Py = map(lambda x:int(x)-1,input().split())
for i in range(M):
    x, y, d = map(lambda x:int(x)-1,input().split())
    grid[x][y].append(d)

########################################################

def print_grid():
    for x in range(N):
        for y in range(N):
            print('[',end='')
            for d in grid[x][y]:
                print(d_to_arrow[d],end='')
            print(']',end=' ')
        print()
    print()
    return

def print_dead_grid():
    for x in range(N):
        for y in range(N):
            print(dead_grid[x][y],end=' ')
        print()
    print()

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def can_go(x,y):
    return in_range(x,y) and (x,y) != (Px,Py) and not dead_grid[x][y]

def copy_duplicate():
    clear_duplicate()
    for x in range(N):
        for y in range(N):
            duplicate_grid[x][y] = grid[x][y][:]
    return

def clear_duplicate():
    for x in range(N):
        for y in range(N):
            duplicate_grid[x][y].clear()
    return

def move_monsters():
    clear_next_grid()
    for x in range(N):
        for y in range(N):
            for d in grid[x][y]:
                moved = False
                for i in range(8):
                    nd = (d + i) % 8
                    nx, ny = x + dxs[nd], y + dys[nd]
                    if can_go(nx,ny):
                        next_grid[nx][ny].append(nd)
                        moved = True
                        break
                if not moved:
                    next_grid[x][y].append(d)
    copy_next_grid()
    return

def copy_next_grid():
    for x in range(N):
        for y in range(N):
            grid[x][y] = next_grid[x][y][:]
    return

def clear_next_grid():
    for x in range(N):
        for y in range(N):
            next_grid[x][y].clear()
    return

def move_pacman():
    global best_kill,Px,Py
    best_move.clear()
    best_kill = -1
    selected_move.clear()

    choose(0,Px,Py,0)

    # print(best_kill)
    # print(best_move)

    for x, y in best_move:
        Px, Py = x, y
        dead_grid[Px][Py] += [3] * len(grid[Px][Py])
        grid[Px][Py].clear()

    return

def choose(n,x,y,kill):
    global best_kill, best_move
    if n == 3:
        if kill > best_kill:
            best_kill = kill
            best_move = selected_move[:]
        return

    for d in [0,2,4,6]:
        nx, ny = x + dxs[d], y + dys[d]
        if in_range(nx,ny):
            overlap = True if (nx,ny) in selected_move else False
            selected_move.append((nx,ny))
            if not overlap:
                choose(n+1,nx,ny,kill+len(grid[nx][ny]))
            else:
                choose(n+1,nx,ny,kill)
            selected_move.pop()
    return


def delete_dead_monsters():
    for x in range(N):
        for y in range(N):
            temp = []
            for elem in dead_grid[x][y]:
                if elem > 1:
                    temp.append(elem-1)
            dead_grid[x][y] = temp[:]
    return

def add_duplicate():
    for x in range(N):
        for y in range(N):
            for elem in duplicate_grid[x][y]:
                grid[x][y].append(elem)
    return

def get_monster_sum():
    return sum([len(grid[x][y]) for x in range(N) for y in range(N)])

########################################################

for i in range(T):
    # print('--------------------',i)
    copy_duplicate()

    move_monsters()
    # print("after move_monster")
    # print_grid()

    move_pacman()
    # print("after move_pacman")
    # print_grid()
    # print(Px,Py)

    delete_dead_monsters()
    # print("after delete_dead")
    # print_dead_grid()

    add_duplicate()
    # print("after duplicate")
    # print_grid()

print(get_monster_sum())