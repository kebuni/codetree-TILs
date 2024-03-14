UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
NO_MONO = (0,0)
OUT_OF_GAME = (100,100,100)

dxs = [-1,1,0,0]
dys = [0,0,-1,1]

N, M, K = map(int,input().split())

grid = [[NO_MONO for i in range(N)] for j in range(N)]
next_player_grid = [[NO_MONO for i in range(N)] for j in range(N)]
player_grid = [[NO_MONO for i in range(N)] for j in range(N)]
direct_priority = []

for x in range(N):
    line = list(map(int,input().split()))
    for y, elem in enumerate(line):
        if elem != 0:
            player_grid[x][y] = (elem,-1)
            grid[x][y] = (elem,K)

first_direction = list(map(int,input().split()))
for i, d in enumerate(first_direction):
    for x in range(N):
        for y in range(N):
            if player_grid[x][y][0] == i+1:
                player_grid[x][y] = (i+1,d-1)

direct_priority.append([[0 for i in range(4)] for j in range(4)])
for i in range(M):
    direct_priority_one = []
    for j in range(4):
        direct_priority_one.append(list(map(lambda x:int(x)-1,input().split())))
    direct_priority.append(direct_priority_one)

#############################################

def print_grid():
    for x in range(N):
        for y in range(N):
            print(grid[x][y],end=' ')
        print()
    print()
    return

def print_player_grid():
    for x in range(N):
        for y in range(N):
            print(player_grid[x][y],end=' ')
        print()
    print()
    return

def move():
    for x in range(N):
        for y in range(N):
            if player_grid[x][y][0] == 0:
                continue
            num, cur_d = player_grid[x][y]
            moved = False

            for d in direct_priority[num][cur_d]:
                nx, ny = x + dxs[d], y + dys[d]
                if in_range(nx,ny) and grid[nx][ny] == NO_MONO:
                    push_next_grid(nx,ny,num,d)
                    moved = True
                    break

            if moved:
                continue

            for d in direct_priority[num][cur_d]:
                nx, ny = x + dxs[d], y + dys[d]
                if in_range(nx,ny) and grid[nx][ny][0] == num:
                    push_next_grid(nx,ny,num,d)
                    break
    return

def decrease():
    for x in range(N):
        for y in range(N):
            num, remain = grid[x][y]
            if num != 0:
                remain -= 1
                if remain == 0:
                    grid[x][y] = (0,0)
                else:
                    grid[x][y] = (num, remain)
    return

def check_end():
    for x in range(N):
        for y in range(N):
            if player_grid[x][y][0] > 1:
                return False
    return True

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def copy_player_grid():
    for x in range(N):
        for y in range(N):
            player_grid[x][y] = next_player_grid[x][y]
            next_player_grid[x][y] = NO_MONO
    return

def new_monoploy():
    for x in range(N):
        for y in range(N):
            if player_grid[x][y][0] != 0:
                grid[x][y] = (player_grid[x][y][0],K+1)
    return

def push_next_grid(x,y,num,d):
    if next_player_grid[x][y] == NO_MONO:
        next_player_grid[x][y] = (num,d)
    else:
        if next_player_grid[x][y] > (num,d):
            next_player_grid[x][y] = (num,d)
    return

#############################################
# print('--------------init-------------')
# print_grid()
# print_player_grid()

ans = -1
for T in range(1,1001):
    move()
    copy_player_grid()
    new_monoploy()
    decrease()

    # print('----------',T,'----------')
    # print_grid()
    # print_player_grid()

    if check_end():
        ans = T
        break
print(ans)