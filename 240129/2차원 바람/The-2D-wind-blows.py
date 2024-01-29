# 입력값 1 조심!

grid = []
dxs = [-1,0,1,0]
dys = [0,1,0,-1]

#############

def print_grid():
    for i in range(N):
        for j in range(M):
            print(grid[i][j], end=' ')
        print()

def in_range(x,y):
    return 0<=x<N and 0<=y<M

def rotate(r1,c1,r2,c2):

    arr = []

    for i in range(c1,c2):
        arr.append(grid[r1][i])
    for i in range(r1,r2):
        arr.append(grid[i][c2])
    for i in range(c2,c1,-1):
        arr.append(grid[r2][i])
    for i in range(r2,r1,-1):
        arr.append(grid[i][c1])

    #print(arr)

    temp = arr[-1]
    for i in range(len(arr)-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = temp

    #print(arr)
    k = 0
    for i in range(c1,c2):
        grid[r1][i] = arr[k]
        k += 1
    for i in range(r1,r2):
        grid[i][c2] = arr[k]
        k += 1
    for i in range(c2,c1,-1):
        grid[r2][i] = arr[k]
        k += 1
    for i in range(r2,r1,-1):
        grid[i][c1] = arr[k]
        k += 1

    #print_grid()

def average(r1,c1,r2,c2):
    temp = [[0]*M for i in range(N)]

    for x in range(r1,r2+1):
        for y in range(c1, c2+1):
            sum = grid[x][y]
            cnt = 1
            for dx, dy in zip(dxs,dys):
                nx = x + dx
                ny = y + dy
                if in_range(nx,ny):
                    sum = sum + grid[nx][ny]
                    cnt = cnt + 1
            temp[x][y] = sum // cnt

    for x in range(r1, r2 + 1):
        for y in range(c1, c2 + 1):
            grid[x][y] = temp[x][y]


#############

N, M, Q = map(int,input().split())

for _ in range(N):
    grid.append(list(map(int,input().split())))

for _ in range(Q):

    r1, c1, r2, c2 = map(int,input().split())

    rotate(r1-1,c1-1,r2-1,c2-1)
    average(r1-1,c1-1,r2-1,c2-1)

print_grid()