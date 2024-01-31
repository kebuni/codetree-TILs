grid = []
temp = []
dxs = [-1,0,1,0]
dys = [0,1,0,-1]

############

def simulate(time):

    global grid, temp

    dist = 2**(time-1)
    init_temp()

    for i in range(N):
        for j in range(N):
            if grid[i][j]:
                temp[i][j] = 1
                spread(i,j,dist)
    for i in range(N):
        for j in range(N):
            grid[i][j] = temp[i][j]
    return

def init_temp():
    for i in range(N):
        for j in range(N):
            temp[i][j] = 0

def spread(x,y,range):
    global temp
    for dx, dy in zip(dxs,dys):
        nx = x + range*dx
        ny = y + range*dy
        if in_range(nx,ny):
            temp[nx][ny] = 1
    #print(temp)

def count_bomb():
    sum = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j]:
                sum += 1
    return sum

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def print_grid():
    for i in range(N):
        for j in range(N):
            print(grid[i][j],end=' ')
        print()

############

N, M, r, c = map(int,input().split())
r = r - 1
c = c - 1

for _ in range(N):
    grid.append([0 for i in range(N)])
    temp.append([0 for i in range(N)])

grid[r][c] = 1

for time in range(1,M+1):
    simulate(time)
    #print_grid()
    #print()

print(count_bomb())