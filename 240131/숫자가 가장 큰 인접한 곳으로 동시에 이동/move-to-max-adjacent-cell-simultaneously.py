grid = []
bids = []
next_bids = []
dxs = [-1,1,0,0]
dys = [0,0,-1,1]

########################
def count_bids():
    cnt = 0
    for i in range(N):
        for j in range(N):
            if bids[i][j]:
                cnt += 1

    return cnt

def print_bids():
    for i in range(N):
        for j in range(N):
            print(bids[i][j],end=' ')
        print()

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def move():
    global bids, next_bids

    clear_next_bids()

    for x in range(N):
        for y in range(N):
            if bids[x][y]: #각각 칸에 대해
                max_num = -1
                max_dir = -1
                for i in range(4):
                    nx = x + dxs[i]
                    ny = y + dys[i]
                    if in_range(nx,ny):
                        if grid[nx][ny] > max_num:
                            max_num = grid[nx][ny]
                            max_dir = i
                # 여기까지 하면 최대로 가는 i가 결정됨
                next_bids[x+dxs[max_dir]][y+dys[max_dir]] += 1

    for i in range(N):
        for j in range(N):
            bids[i][j] = next_bids[i][j]


def crash():
    global bids

    for i in range(N):
        for j in range(N):
            if bids[i][j] > 1:
                bids[i][j] = 0

def clear_next_bids():
    global next_bids
    for i in range(N):
        for j in range(N):
            next_bids[i][j] = 0

########################

N, M, T = map(int,input().split())

for _ in range(N):
    grid.append(list(map(int,input().split())))
    bids.append([0 for i in range(N)])
    next_bids.append([0 for i in range(N)])

for _ in range(M):
    r, c = map(int,input().split())
    bids[r-1][c-1] = 1

for _ in range(T):
    move()
    crash()

print(count_bids())