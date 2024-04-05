import sys

BLANK = 0
WALL = 1
EXIT = 2
EXITED = (100,100)
OUT_OF_GRID = 100

RX, RY = -1, -1
BX, BY = -1, -1
dxs = [-1,0,1,0]
dys = [0,1,0,-1]

N, M = map(int,input().split())
grid = [[0 for j in range(M)] for i in range(N)]
visited = [[[[[False for i_d in range(4)]
              for i_by in range(M)]
             for i_bx in range(N)]
            for i_ry in range(M)]
           for i_rx in range(N)]
for x in range(N):
    line = list(input())
    for y, elem in enumerate(line):
        if elem == '#':
            grid[x][y] = WALL
        elif elem == 'B':
            BX, BY = x, y
        elif elem == 'R':
            RX, RY = x, y
        elif elem == 'O':
            grid[x][y] = EXIT

################################

def print_grid(A):
    for x in range(N):
        for y in range(M):
            print(A[x][y],end=' ')
        print()
    print()

def find_min_number(n,rx,ry,bx,by,d):
    global ans
    # print("[find_min_number]",n,rx,ry,bx,by,d)
    # 11번째 기울여야 하는 상황이면 return 합니다.
    if n == 11:
        # print("11th try. return")
        return

    # 현재 상태를 visited에 기록합니다.
    visited[rx][ry][bx][by][d] = True

    # rx,ry,bx,by인 상황에서 d로 기울였을 때 상태를 계산합니다.
    nrx, nry, nbx, nby = cal_next_state(rx,ry,bx,by,d)
    # print("nrx,nry,nbx,nby:",nrx,nry,nbx,nby)

    # 만약 빨간 사탕만 나가게 됐다면 ans를 업데이트하고 return 합니다.
    if (nrx,nry) == EXITED and (nbx, nby) != EXITED:
        ans = min(ans,n)
        # print("new ans!",ans)
        return
    elif (nbx, nby) == EXITED:
        return

    # 그렇지 않다면 4방향에 대해 기울이는 것을 이어갑니다.
    # 함수 호출전 혹시 visited된 상태라면 넘어갑니다.
    for nd in range(4):
        ##if nd != d and not visited[nrx][nry][nbx][nby][nd]:
        if nd != d:
            find_min_number(n+1,nrx,nry,nbx,nby,nd)

    return

def cal_next_state(rx,ry,bx,by,d):
    nrx, nry, nbx, nby = 100, 100, 100, 100
    if d == 0 or d == 3: # 좌상단으로 이동시 좌상단 사탕 먼저 이동
        if (rx,ry) < (bx,by):
            nrx, nry = cal_next_state_one(rx,ry,bx,by,d)
            # print("nrx,nry:",nrx,nry)
            nbx, nby = cal_next_state_one(bx,by,nrx,nry,d)
            # print("nbx,nby:", nbx, nby)
        else:
            nbx, nby = cal_next_state_one(bx, by, rx, ry, d)
            # print("nbx,nby:", nbx, nby)
            nrx, nry = cal_next_state_one(rx, ry, nbx, nby, d)
            # print("nrx,nry:", nrx, nry)

    else: # 우하단으로 이동시 우하단 사탕 먼저 이동
        if (rx,ry) > (bx,by):
            nrx, nry = cal_next_state_one(rx, ry, bx, by, d)
            # print("nrx,nry:", nrx, nry)
            nbx, nby = cal_next_state_one(bx, by, nrx, nry, d)
            # print("nbx,nby:", nbx, nby)
        else:
            nbx, nby = cal_next_state_one(bx, by, rx, ry, d)
            # print("nbx,nby:", nbx, nby)
            nrx, nry = cal_next_state_one(rx, ry, nbx, nby, d)
            # print("nrx,nry:", nrx, nry)

    return nrx, nry, nbx, nby

def cal_next_state_one(x,y,ox,oy,d):
    while True:
        nx, ny = x + dxs[d], y + dys[d]
        # 다음 위치가 벽이거나 다른 사탕이면 갈 수 없습니다.
        if grid[nx][ny] == WALL or (nx,ny) == (ox,oy):
            break
        elif grid[nx][ny] == EXIT:
            x, y = OUT_OF_GRID, OUT_OF_GRID
            break
        else:
            x, y = nx, ny
    return x, y

################################

ans = sys.maxsize

for d in range(4):
    find_min_number(1,RX,RY,BX,BY,d)

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)