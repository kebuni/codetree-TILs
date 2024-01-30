grid = []
dxs = [-1,0,1,0]
dys = [0,1,0,-1]

###########

def print_grid():
    for i in range(N):
        for j in range(N):
            print(grid[i][j],end=' ')
        print()

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def explode(r,c):
    size = grid[r][c]
    grid[r][c] = 0

    for dx,dy in zip(dxs,dys):
        x, y = r, c
        for i in range(size-1):
            nx = x + dx
            ny = y + dy
            if in_range(nx,ny):
                x = nx
                y = ny
                grid[x][y] = 0
            else:
                break

def fall():

    global grid

    temp = [[0]*N for _ in range(N)]

    for col in range(N):
        end_of_arr = N-1
        for row in range(N-1,-1,-1):
            if grid[row][col] != 0:
                temp[end_of_arr][col] = grid[row][col]
                end_of_arr -= 1

    grid = temp

###########

N = int(input())

for _ in range(N):
    grid.append(list(map(int,input().split())))

r, c = map(int,input().split())

explode(r-1,c-1)
#print_grid()

fall()
print_grid()