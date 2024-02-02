NO_BID = (0,0,0)
grid = []
next_grid = []
dxs = [-1,0,1,0]
dys = [0,1,0,-1]
directs = {'U':0, 'R':1, 'D':2, 'L':3}
max_weight = -1
####################

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def print_grid():
    for i in range(N):
        for j in range(N):
            print(grid[i][j],end=' ')
        print()

def print_next_grid():
    for i in range(N):
        for j in range(N):
            print(next_grid[i][j],end=' ')
        print()

def count_grid():
    cnt = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j][0]:
                cnt += 1
    return cnt

def move(x,y):
    global next_grid
    idx, w, d = grid[x][y]
    nx = x + dxs[d]
    ny = y + dys[d]
    if not in_range(nx,ny):
        d = (d + 2) % 4
        next_grid[x][y].append((idx,w,d))
    else:
        x = x + dxs[d]
        y = y + dys[d]
        next_grid[x][y].append((idx,w,d))


def copy():
    global grid
    for i in range(N):
        for j in range(N):
            if len(next_grid[i][j]):
                grid[i][j] = next_grid[i][j][0]
            else:
                grid[i][j] = NO_BID
    return

def collide():
    global next_grid, max_weight
    for i in range(N):
        for j in range(N):
            if len(next_grid[i][j]):
                next_grid[i][j].sort(reverse=True)
                new_idx = next_grid[i][j][0][0]
                new_w = sum(list(map(lambda x:x[1],next_grid[i][j])))
                new_d = next_grid[i][j][0][2]
                next_grid[i][j] = [(new_idx,new_w,new_d)]
                max_weight = max(new_w,max_weight)
                

    return

def initialize_next_grid():
    global next_grid
    for i in range(N):
        for j in range(N):
            next_grid[i][j] = []

####################
N, M, T = map(int,input().split())

for i in range(N):
    grid.append([(0,0,0) for j in range(N)]) #(n,w,d)
    next_grid.append([[] for j in range(N)]) #(n,w,d)

for i in range(M):
    r,c,d,w = input().split()
    max_weight = max(max_weight,int(w))
    grid[int(r)-1][int(c)-1] = (i+1,int(w),directs[d])

# print_grid()
# print()
# print_next_grid()
# print()

for _ in range(T):
    #print_grid()
    initialize_next_grid()

    for x in range(N):
        for y in range(N):
            if grid[x][y][0]:
                move(x,y)

    collide()
    # print_next_grid()
    # print()

    copy()
    # print_next_grid()
    # print()

    # print_grid()
    # print()
    # print_next_grid()
    # print()

# print('---------end----------')
print(count_grid(),max_weight)