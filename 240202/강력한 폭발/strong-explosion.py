grid = []
bomb_grid = []
bomb_list = []
bomb1 = [(-2,0),(-1,0),(0,0),(1,0),(2,0)]
bomb2 = [(0,0),(-1,0),(0,1),(1,0),(0,-1)]
bomb3 = [(0,0),(-1,-1),(-1,1),(1,-1),(1,1)]
bomb_num = 0
ans = 0
#######################

def print_grid():
    for i in range(N):
        for j in range(N):
            print(grid[i][j],end=' ')
        print()

def print_bomb_grid():
    for i in range(N):
        for j in range(N):
            print(bomb_grid[i][j],end=' ')
        print()

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def make_bomb_list():
    global bomb_list
    for i in range(N):
        for j in range(N):
            if grid[i][j]:
                bomb_list.append((i,j))

def bomb_recursive(n):
    global ans
    if n == bomb_num:
        ans = max(ans,count())
        #print_bomb_grid()
        #print()
        return

    bomb(n,1,1)
    bomb_recursive(n+1)
    bomb(n,1,0)

    bomb(n, 2, 1)
    bomb_recursive(n + 1)
    bomb(n, 2, 0)

    bomb(n, 3, 1)
    bomb_recursive(n + 1)
    bomb(n, 3, 0)

    return

def bomb(idx,type,onoff):
    global bomb_grid
    x, y = bomb_list[idx]

    if type==1:
        bomb_type = bomb1
    elif type ==2:
        bomb_type = bomb2
    else:
        bomb_type = bomb3

    for dx,dy in bomb_type:
        nx = x + dx
        ny = y + dy
        if in_range(nx,ny):
            bomb_grid[nx][ny][type-1] = onoff

def count():
    cnt = 0
    for i in range(N):
        for j in range(N):
            if bomb_grid[i][j][0] or bomb_grid[i][j][1] or bomb_grid[i][j][2]:
                cnt += 1

    return cnt

#######################

N = int(input())
for _ in range(N):
    grid.append(list(map(int,input().split())))
    bomb_grid.append([[0,0,0] for i in range(N)])

make_bomb_list()
bomb_num = len(bomb_list)

bomb_recursive(0)
print(ans)