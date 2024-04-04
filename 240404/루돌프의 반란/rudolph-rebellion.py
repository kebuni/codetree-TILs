import sys

dxs = [-1,-1,0,1,1,1,0,-1]
dys = [0,1,1,1,0,-1,-1,-1]
INT_MAX = sys.maxsize

N, M, P, C, D = map(int,input().split())
grid = [[0 for i in range(N)] for j in range(N)]
RX, RY = map(lambda x:int(x)-1,input().split())
grid[RX][RY] = -1
santa_pos = [(-1,-1) for i in range(P+1)]
for i in range(P):
    idx, x, y = map(int,input().split())
    santa_pos[idx] = (x-1,y-1)
    grid[x-1][y-1] = idx
santa_status = [0 for i in range(P+1)]
santa_score = [0 for i in range(P+1)]

#################################################

def print_grid(A):
    for x in range(N):
        for y in range(N):
            print(A[x][y],end=' ')
        print()
    print()
    return

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def can_go(x,y):
    return in_range(x,y) and grid[x][y] <= 0

def dist(x1,y1,x2,y2):
    return (x1-x2)**2 + (y1-y2)**2

def move_rudolph():
    global RX, RY
    # 가장 가까운 산타 선정
    sx, sy = INT_MAX, INT_MAX
    min_dist = INT_MAX
    for x in range(N-1,-1,-1):
        for y in range(N-1,-1,-1):
            if grid[x][y] > 0:
                temp_dist = dist(RX,RY,x,y)
                if temp_dist < min_dist:
                    sx, sy = x, y
                    min_dist = temp_dist

    # 그 산타에게 가장 가까워지는 방향으로 이동
    bx, by, bd = INT_MAX, INT_MAX, INT_MAX
    min_dist2 = INT_MAX
    for d in range(8):
        nx, ny = RX + dxs[d], RY + dys[d]
        temp_dist = dist(sx,sy,nx,ny)
        if temp_dist < min_dist2:
            bx, by = nx, ny
            bd = d
            min_dist2 = temp_dist

    # 충돌이 일어난다면 충돌처리 해야 합니다
    if grid[bx][by] != 0:
        rudolph_crash(bx,by,bd)

    grid[bx][by] = -1
    grid[RX][RY] = 0
    RX, RY = bx, by
    return

def rudolph_crash(x,y,d):
    # x, y에 있는 산타에게 루돌프가 d 방향으로 충돌했습니다.
    idx = grid[x][y]
    # 거기 있는 산타에게 점수 추가
    santa_score[idx] += C
    # 거기 있는 산타 기절 상태
    santa_status[idx] = 2
    # 튕겨져 날아간 위치가 밖이면 탈락처리
    nx, ny = x + C * dxs[d], y + C * dys[d]
    if not in_range(nx,ny):
        santa_status[idx] = -1
    # 튕겨져 날아간 위치가 안이면 상호작용처리
    else:
        interaction(idx, nx, ny, d)
    return

def santa_crash(idx,x,y,d):
    # x, y에 있는 루돌프에게 idx번 산타가 d 방향으로 충돌했습니다.
    # idx 산타에게 점수 추가
    santa_score[idx] += D
    # idx 산타 기절 상태
    santa_status[idx] = 2
    # 튕겨져 날아간 위치가 밖이면 탈락처리
    nd = (d + 4) % 8
    nx, ny = x + D * dxs[nd], y + D * dys[nd]
    if not in_range(nx,ny):
        santa_status[idx] = -1
    # 튕겨져 날아간 위치가 안이면 상호작용처리
    else:
        interaction(idx,nx,ny,nd)
    return

def interaction(idx,x,y,d):
    # print("interaction:",idx,x,y,d)
    # x, y위치에 산타가 d 방향으로 날아왔습니다.
    # x, y 위치에 더 이상 산타가 없을 때까지 상호작용처리 해야합니다.

    while grid[x][y]: # idx가 들어와야할 현재 위치에 누가 있다면?
        nidx = grid[x][y] # 먼저 와있는 사람은 nidx라고 합시다
        grid[x][y] = idx # x,y에 idx를 일단 넣습니다.
        santa_pos[idx] = (x,y)

        nx, ny = x + dxs[d], y + dys[d] # nidx가 와야할 자리 입니다.
        if not in_range(nx,ny): # 만약 nidx가 범위 밖으로 나가게 된다면
            santa_pos[nidx] = -1 # nidx는 탈락입니다.
            return # 상호작용을 중단합니다.
        else: # nidx가 갈 자리가 있다면
            idx = nidx # nidx를 idx로 두고 다시 봅시다.
            x, y = nx, ny

    # 여기에 왔다는 것은 마지막 사람이 빈자리에 갔다는 것이죠.
    # 해당 자리에 idx를 넣고 마무리합니다.
    grid[x][y] = idx
    santa_pos[idx] = (x,y)
    return

def move_santas():
    for idx in range(1,P+1):

        # print("now santa",idx,"is moving")

        # 기절하거나 탈락한 산타는 넘어갑니다.
        if santa_status[idx] != 0:
            continue

        moved = False
        x, y = santa_pos[idx]
        bx, by, bd = x, y, 0
        min_dist = dist(RX,RY,x,y)
        for d in [0,2,4,6]:
            nx, ny = x + dxs[d], y + dys[d]
            if can_go(nx,ny):
                temp_dist = dist(RX,RY,nx,ny)
                if temp_dist < min_dist:
                    moved = True
                    min_dist = temp_dist
                    bx, by, bd = nx, ny, d

        # print("going to",bx,by,bd)

        if moved:
            grid[x][y] = 0

        if grid[bx][by] == -1:
            santa_crash(idx,bx,by,bd)
        else:
            grid[bx][by] = idx
            santa_pos[idx] = (bx,by)


    return

def update_status():
    for i in range(1,P+1):
        if santa_status[i] > 0:
            santa_status[i] -= 1

    for i in range(1,P+1):
        if santa_status[i] != -1:
            santa_score[i] += 1
    return

def check_end():
    for i in range(1,P+1):
        if santa_status[i] != -1:
            return False
    return True

def print_ans():
    for i in range(1,P+1):
        print(santa_score[i],end=' ')
    return

#################################################

# print("init--------------")
# print_grid(grid)
# print("RX,RV: ",RX,RY)
# print("pos: ",santa_pos)
# print("status: ",santa_status)
# print("score: ", santa_score)

for t in range(M):
    # print('----------------',t)

    move_rudolph()
    # print("after move_rudolph")
    # print_grid(grid)
    # print("RX,RV: ",RX,RY)
    # print("pos: ",santa_pos)
    # print("status: ",santa_status)
    # print("score: ", santa_score)

    move_santas()
    # print("after move_santa")
    # print_grid(grid)
    # print("pos: ", santa_pos)
    # print("status: ", santa_status)
    # print("score: ", santa_score)

    update_status()
    # print("after update status")
    # print("status: ",santa_status)
    # print("score: ", santa_score)

    if check_end():
        # print("check_end")
        break

print_ans()