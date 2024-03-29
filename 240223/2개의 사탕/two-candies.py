import copy

BLANK = 0
WALL = 1
RED = 2
BLUE = 3
EXIT = 4

dxs = [-1,0,1,0]
dys = [0,1,0,-1]

ans = 100

EXIT_POS = (100,100)
red_pos = (0,0)
blue_pos = (0,0)

grid = []

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

def blue_escaped():
    return blue_pos == EXIT_POS

def red_escaped():
    return red_pos == EXIT_POS

def move(idx,d):
    ### x,y에 있는 애를 d 방향으로 최대한 밀어낸다
    global red_pos, blue_pos
    x, y = red_pos if idx == RED else blue_pos

    nx = x + dxs[d]
    ny = y + dys[d]

    while can_go(nx,ny):
        # exit이면 위치 EXIT_POS로 바꿈
        if grid[nx][ny] == EXIT:
            if idx == RED:
                red_pos = EXIT_POS
            else:
                blue_pos = EXIT_POS
            return

        # exit이 아니면...
        x, y = nx, ny

        nx = x + dxs[d]
        ny = y + dys[d]

    if idx == RED:
        red_pos = (x,y)
    else:
        blue_pos = (x,y)
    return

def tilt(d):
    # print("before tilt:")
    # print_grid()
    if d == 0 or d == 3:
        if red_pos < blue_pos:
            move(RED,d)
            move(BLUE,d)
        else:
            move(BLUE, d)
            move(RED, d)
    else:
        if red_pos < blue_pos:
            move(BLUE, d)
            move(RED,d)
        else:
            move(RED, d)
            move(BLUE, d)

    # print("after tilt",d)
    # print_grid()
    # print('------------------------------')
    return

def can_go(x,y):
    return in_range(x,y) and grid[x][y] != WALL and (x,y) != red_pos and (x,y) != blue_pos

def in_range(x,y):
    return 0<=x<N and 0<=y<M

def find_min(n,prev):
    global ans, grid, red_pos, blue_pos
    if n == 11:
        return

    # 만약 파란사탕이 없어졌으면 더 이상 볼 필요가 없다
    if blue_escaped():
        #print("here1")
        return

    # 파란 사탕이 있는게 보장됐을때, 빨간 사탕이 없으면 ans 업데이트하고 종료
    if red_escaped():
        #print("done!!",n)
        ans = min(ans,n)
        return

    # 아직 둘다 남아있으면, 4방향 중 이전에 안해본 3방향 기울여본다
    for d in range(4):

        if prev != d: #전에 기울여 본 방향이 아니면,
            temp_red_pos = red_pos
            temp_blue_pos = blue_pos
            tilt(d)
            find_min(n+1,d)
            red_pos = temp_red_pos
            blue_pos = temp_blue_pos

    return

def print_grid():
    temp = copy.deepcopy(grid)
    if red_pos != EXIT_POS:
        temp[red_pos[0]][red_pos[1]] = 'R'
    if blue_pos != EXIT_POS:
        temp[blue_pos[0]][blue_pos[1]] = 'B'
    for i in range(N):
        for j in range(M):
            print(temp[i][j],end=' ')
        print()
    print()

#######################

N, M = map(int,input().split())

for i in range(N):
    line = list(map(char_to_int, input()))
    for j, elem in enumerate(line):
        if elem == RED:
            red_pos = (i,j)
            line[j] = BLANK
        elif elem == BLUE:
            blue_pos = (i,j)
            line[j] = BLANK
    grid.append(line)

find_min(0,5)

if ans == 100:
    print(-1)
else:
    print(ans)