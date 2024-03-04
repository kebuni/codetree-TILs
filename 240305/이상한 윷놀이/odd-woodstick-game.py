import sys

N, K = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
player_grid = [[[] for i in range(N)] for j in range(N)]
player_loc = []

dxs = [0,0,-1,1]
dys = [1,-1,0,0]

for i in range(K):
    x, y, d = map(int,input().split())
    player_loc.append((x-1,y-1,d-1))
    player_grid[x-1][y-1].append((i))

###############################################
def in_range(x,y):
    return 0<=x<N and 0<=y<N

def check_end():
    for i in range(N):
        for j in range(N):
            if len(player_grid[i][j]) >= 4:
                return True
    return False

def move(idx):
    # 플레이어 idx의 위치를 찾습니다.
    x, y, d = player_loc[idx]
    # 현재 플레이어가 몇번째로 쌓여있는지 확인합니다.
    stack_i = player_grid[x][y].index(idx)

    nx, ny = x + dxs[d], y + dys[d]

    if not in_range(nx,ny) or grid[nx][ny] == 2:
        d = d^1 # 방향을 반대로 전환
        nx, ny = x + dxs[d], y + dys[d]
        player_loc[idx] = (x, y, d)

    if not in_range(nx,ny) or grid[nx][ny] == 2:
        q = 0
    elif grid[nx][ny] == 1:
        moving_player = player_grid[x][y][stack_i:]
        player_grid[x][y] = player_grid[x][y][:stack_i]
        moving_player.reverse()
        for p in moving_player:
            _, _, pd = player_loc[p]
            player_loc[p] = (nx,ny,pd)
        player_grid[nx][ny] += moving_player
    else:
        moving_player = player_grid[x][y][stack_i:]
        player_grid[x][y] = player_grid[x][y][:stack_i]
        for p in moving_player:
            _, _, pd = player_loc[p]
            player_loc[p] = (nx,ny,pd)
        player_grid[nx][ny] += moving_player

    return

def print_player_grid():
    for i in range(N):
        for j in range(N):
            print(player_grid[i][j],end=' ')
        print()
    print()

###############################################

#print_player_grid()

for t in range(1,1001):
    #print("now turn : ",t)
    for i in range(K):
        move(i)
        #print_player_grid()
        if check_end():
            #print("done!!")
            print(t)
            sys.exit(0)

#print("done!!")
print(-1)