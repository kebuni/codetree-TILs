grid = []
ans = -1
dxs = [-1,0,1,0]
dys = [0,1,0,-1]
##################

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def print_grid(x,y):
    temp = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            temp[i][j] = grid[i][j]
    temp[x][y] = 3
    for i in range(N):
        for j in range(N):
            print(temp[i][j],end=' ')
        print()
    print()

def simulate(original_x,original_y,direct):
    cnt = 1
    x = original_x
    y = original_y
    #print_grid(x, y)
    while True:
        x = x + dxs[direct]
        y = y + dys[direct]
        cnt += 1
        if not in_range(x,y):
            break
        if grid[x][y]:
            direct = reflect(direct,grid[x][y])
        #print_grid(x,y)

    #print("end!",cnt)
    return cnt

def reflect(direct,mirror):
    if mirror == 1:
        if direct == 0:
            return 1
        elif direct == 1:
            return 0
        elif direct == 2:
            return 3
        else:
            return 2
    else:
        if direct == 0:
            return 3
        elif direct == 3:
            return 0
        elif direct == 2:
            return 1
        else:
            return 2

##################

N = int(input())
for _ in range(N):
    grid.append(list(map(int,input().split())))

for i in range(N):
    ans = max(ans,simulate(0,i,2))

for i in range(N):
    ans = max(ans,simulate(i,N-1,3))

for i in range(N-1,-1,-1):
    ans = max(ans, simulate(N-1, i, 0))

for i in range(N-1,-1,-1):
    ans = max(ans, simulate(i, 0, 1))

print(ans)