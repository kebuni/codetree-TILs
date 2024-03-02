import sys

dxs = [-1,0,1,0]
dys = [0,1,0,-1]

ans = sys.maxsize

N, M = map(int,input().split())

grid = []
temp = [[0 for i in range(M)] for j in range(N)]
players = []
opposite = []
selected = []

for x in range(N):
    line = list(map(int,input().split()))
    for y, elem in enumerate(line):
        if elem in [1,2,3,4,5]:
            players.append((elem,x,y))
        elif elem == 6:
            opposite.append((x,y))
    grid.append(line)

player_num = len(players)

##################################################

def in_range(x,y):
    return 0<=x<N and 0<=y<M

def can_go(x,y):
    return in_range(x,y) and grid[x][y] != 6

def init_temp():
    global temp
    for i in range(N):
        for j in range(M):
            temp[i][j] = 0

    for _,x,y in players:
        temp[x][y] = 1

    for x,y in opposite:
        temp[x][y] = 1

    return

def cal_size():
    sum = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j]==0:
                sum += 1
    return sum

def find_min(n):
    # 모든 말의 방향을 다 정했으면
    if n == player_num:
        init_temp()
        simulate()
        #print_temp()
        global ans
        ans = min(ans,cal_size())
        return

    for i in range(4):
        selected.append(i)
        find_min(n+1)
        selected.pop()

    return

def simulate():
    #방향이 다 정해졌으니 temp를 그려봅시다

    # 모든 말에 대하여,
    for idx in range(player_num):

        # 그말의 타입, x, y를 구합니다.
        player_type, original_x, original_y = players[idx]
        #print(player_type,x,y)
        # 그 말이 가야할 방향 리스트
        directs = []
        if player_type == 1:
            directs.append(selected[idx])
        elif player_type == 2:
            directs.append(selected[idx])
            directs.append((selected[idx] + 2) % 4)
        elif player_type == 3:
            directs.append(selected[idx])
            directs.append((selected[idx] + 1) % 4)
        elif player_type == 4:
            directs.append(selected[idx])
            directs.append((selected[idx] + 1) % 4)
            directs.append((selected[idx] + 2) % 4)
        else:
            directs.append(0)
            directs.append(1)
            directs.append(2)
            directs.append(3)

        # 가야할 방향이 정해졌으니 temp를 그려봅시다
        for d in directs:
            x, y = original_x, original_y
            temp[x][y] = 1
            nx = x + dxs[d]
            ny = y + dys[d]
            while can_go(nx,ny):
                x, y = nx, ny
                temp[x][y] = 1
                nx, ny = x + dxs[d], y + dys[d]

    return

def print_temp():
    for i in range(N):
        for j in range(M):
            print(temp[i][j], end=' ')
        print()
    print()

##################################################

find_min(0)
print(ans)