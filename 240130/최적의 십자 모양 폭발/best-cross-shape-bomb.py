grid = []
grid_copy = []
ans = -1
dxs = [0,1,0,-1]
dys = [1,0,-1,0]
################
def copy_grid():
    global grid_copy
    for i in range(N):
        for j in range(N):
            grid_copy[i][j] = grid[i][j]
    return

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def explode(original_x,original_y):
    global grid_copy
    size = grid_copy[original_x][original_y]
    for dx, dy in zip(dxs, dys):
        x = original_x
        y = original_y
        grid_copy[x][y] = 0
        for _ in range(size-1):
            nx = x + dx
            ny = y + dy
            if not in_range(nx,ny):
                break
            x = nx
            y = ny
            grid_copy[x][y] = 0

    return

def fall():
    global grid_copy
    temp = [[0]*N for i in range(N)]
    for j in range(N):
        cnt = N - 1
        for i in range(N-1,-1,-1):
            if grid_copy[i][j]:
                temp[cnt][j] = grid_copy[i][j]
                cnt -= 1
    for i in range(N):
        for j in range(N):
            grid_copy[i][j] = temp[i][j]
    return

def count_pair():
    cnt = 0
    for x in range(N):
        for y in range(N):
            pivot = grid_copy[x][y]
            if pivot:
                if x != N-1:
                    if grid_copy[x+1][y] == pivot:
                        cnt += 1
                if y != N-1:
                    if grid_copy[x][y+1] == pivot:
                        cnt += 1

    return cnt

def print_grid(num):
    if num == 0:
        for i in range(N):
            for j in range(N):
                print(grid[i][j],end=' ')
            print()
    else:
        for i in range(N):
            for j in range(N):
                print(grid_copy[i][j],end=' ')
            print()
    return

################
N = int(input())
for _ in range(N):
    grid.append(list(map(int,input().split())))
    grid_copy.append([0]*N)

for i in range(N):
    for j in range(N):
        copy_grid()
        explode(i,j)
        fall()
        ans = max(ans,count_pair())

print(ans)