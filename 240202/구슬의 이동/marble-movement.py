grid = []
next_grid = []
directs = {'U':0, 'R':1, 'D':2, 'L':3}
dxs = [-1,0,1,0]
dys = [0,1,0,-1]

####################

def print_grid():
    for i in range(N):
        for j in range(N):
            print(grid[i][j],end=' ')
        print()

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def cnt_grid():
    cnt = 0
    for i in range(N):
        for j in range(N):
            cnt += len(grid[i][j])
    return cnt

def initialize_next_grid():
    global next_grid
    for i in range(N):
        for j in range(N):
            next_grid[i][j].clear()

def move(x,y,bid):
    global next_grid
    speed, idx, direct = bid
    for i in range(speed):
        nx = x+dxs[direct]
        ny = y+dys[direct]
        if not in_range(nx,ny): #만약 새 위치가 범위 밖이면
            direct = (direct + 2)%4
        x = x+dxs[direct]
        y = y+dys[direct]
    # 최종 위치가 결정됨
    next_grid[x][y].append((speed,idx,direct))
    return

def remove():
    global grid
    for i in range(N):
        for j in range(N):
            grid[i][j].sort(reverse=True)
            if len(grid[i][j]) > K:
                grid[i][j] = grid[i][j][:K]
    return

def copy():
    global grid,next_grid
    for i in range(N):
        for j in range(N):
            grid[i][j] = next_grid[i][j].copy()

    initialize_next_grid()
    return

####################

N, M, T, K = map(int,input().split())

for _ in range(N):
    grid.append([[] for i in range(N)])
    next_grid.append([[] for j in range(N)])
for i in range(M):
    r,c,d,v = input().split()
    grid[int(r)-1][int(c)-1].append((int(v),i+1,directs[d])) # v,i,d

# print_grid()
for _ in range(T):
    for i in range(N):
        for j in range(N):
            for bid in grid[i][j]: # 각 칸에 있는 구슬들에 대하여
                move(i,j,bid) #각 구슬마다 이동, next에 저장
    
    #모든 구슬의 이동이 끝났으면 제거 작업
    copy()
    remove()
    # print_grid()
    # print()

# print('################end################')
print(cnt_grid())