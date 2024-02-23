import copy

BLANK = 0
WALL = 1
RED = 2
BLUE = 3
EXIT = 4

dxs = [-1,0,1,0]
dys = [0,1,0,-1]

ans = 100

#######################

def char_to_int(elem):
    if elem == 'O':
        return EXIT
    elif elem == '#':
        return WALL
    elif elem == 'R':
        return RED
    elif elem == 'B':
        return BLUE
    else:
        return BLANK

def print_grid():
    for i in range(N):
        for j in range(M):
            print(grid[i][j],end=' ')
        print()
    print()

def exist(elem):
    for i in range(N):
        for j in range(M):
            if grid[i][j] == elem:
                return True
    return False

def move(x,y,d):
    ### x,y에 있는 애를 d 방향으로 최대한 밀어낸다
    nx = x + dxs[d]
    ny = y + dys[d]

    while can_go(nx,ny):
        # exit이면 지우고 나감
        if grid[nx][ny] == EXIT:
            grid[x][y] = BLANK
            return

        # exit이 아니면...
        grid[nx][ny] = grid[x][y]
        grid[x][y] = BLANK

        x, y = nx, ny

        nx = x + dxs[d]
        ny = y + dys[d]

    return

def tilt(d):
    #print("before tilt:")
    #print_grid()
    if d == 0 or d == 3:
        for x in range(N):
            for y in range(M):
                if grid[x][y] == RED or grid[x][y] == BLUE:
                    move(x,y,d)
    else:
        for x in range(N-1,-1,-1):
            for y in range(M-1,-1,-1):
                if grid[x][y] == RED or grid[x][y] == BLUE:
                    move(x,y,d)

    # print("after tilt",d)
    # print_grid()
    # print('------------------------------')
    return

def can_go(x,y):
    return grid[x][y] == BLANK or grid[x][y] == EXIT

def find_min(n,prev):
    global ans, grid
    if n == 11:
        return

    # 만약 파란사탕이 없어졌으면 더 이상 볼 필요가 없다
    if not exist(BLUE):
        return

    # 파란 사탕이 있는게 보장됐을때, 빨간 사탕이 없으면 ans 업데이트하고 종료
    if not exist(RED):
        #print("done!!")
        ans = min(ans,n)
        return

    # 아직 둘다 남아있으면, 4방향 중 이전에 안해본 3방향 기울여본다
    for d in range(4):

        if prev != d: #전에 기울여 본 방향이 아니면,
            temp = copy.deepcopy(grid)
            tilt(d)
            find_min(n+1,d)
            grid = copy.deepcopy(temp)

    return

#######################

N, M = map(int,input().split())

grid = [list(map(char_to_int,input())) for i in range(N)]

find_min(0,5)

if ans == 100:
    print(-1)
else:
    print(ans)