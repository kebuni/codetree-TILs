grid = []
next_grid = []
dxs = [-1,0,1,0]
dys = [0,1,0,-1]
directs = {'U':0, 'R':1, 'D':2, 'L':3}
N = 0
M = 0

######################
def initialize():
    global grid, next_grid
    grid.clear()
    next_grid.clear()

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def print_grid():
    for i in range(N):
        for j in range(N):
            print(f'{grid[i][j]:2}',end=' ')
        print()

def move():
    global next_grid
    init_next_grid()

    for x in range(N):
        for y in range(N):
            cur = grid[x][y]
            if cur != -1: #구슬이 있다면
                nx = x + dxs[cur]
                ny = y + dys[cur]
                #print(nx,ny)
                if not in_range(nx,ny): # 범위 밖이면 방향만 변화
                    next_grid[x][y].append((cur+2)%4)
                else: #갈수 있으면
                    next_grid[nx][ny].append(cur)

def remove():
    global next_grid
    for i in range(N):
        for j in range(N):
            if len(next_grid[i][j])>=2:
                next_grid[i][j] = []

def copy():
    global grid
    for i in range(N):
        for j in range(N):
            if len(next_grid[i][j]):
                grid[i][j] = next_grid[i][j][0]
            else:
                grid[i][j] = -1

def count():
    cnt = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] != -1:
                cnt += 1
    return cnt

def init_next_grid():
    global next_grid
    for i in range(N):
        for j in range(N):
            next_grid[i][j] = []

######################

CaseNum = int(input())
for _ in range(CaseNum):
    initialize()
    N, M = map(int,input().split())
    for i in range(N):
        grid.append([-1 for j in range(N)])
        next_grid.append([[] for k in range(N)])
    for i in range(M):
        r,c,d = input().split()
        r = int(r); c = int(c)
        grid[r-1][c-1] = directs[d]

    #print_grid()
    #print()

    for i in range(2*N):
        move()
        remove()
        copy()
        #print_grid()
        #print()
    #print("end###################")
    print(count())