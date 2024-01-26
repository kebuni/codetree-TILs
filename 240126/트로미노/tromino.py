n, m = map(int,input().split())

grid = []
max = -1

def tromino1(x,y):
    global max
    temp = grid[x][y] + grid[x][y+1] + grid[x+1][y] + grid[x+1][y+1]
    temp = temp - min(grid[x][y],grid[x][y+1],grid[x+1][y],grid[x+1][y+1])

    if temp > max:
        max = temp

def tromino2_vertical(x,y):
    global max
    temp = grid[x][y] + grid[x+1][y] + grid[x+2][y]

    if temp > max:
        max = temp

def tromino2_horizon(x,y):
    global max
    temp = grid[x][y] + grid[x][y+1] + grid[x][y+2]

    if temp > max:
        max = temp

for i in range(n):
    grid.append(list(map(int,input().split())))

for i in range(n-1):
    for j in range(m-1):
        for k in range(4):
            tromino1(i,j)

for i in range(n-2):
    for j in range(m):
        tromino2_vertical(i,j)

for i in range(n):
    for j in range(m-2):
        tromino2_horizon(i,j)

print(max)