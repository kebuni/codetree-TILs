from collections import deque

FRONT = 0
DOWN = 1
RIGHT = 2

N, M = map(int,input().split())
grid = [list(map(int,input().split())) for i in range(N)]

cube = {FRONT:2,DOWN:6,RIGHT:3}
cx, cy = 0, 0
cd = 0

visited = [[False for i in range(N)] for j in range(N)]
q = deque()
score = 0

dxs = [0,1,0,-1]
dys = [1,0,-1,0]
##########################################

def roll_cube(direct):
    global cx, cy, cd

    # 큐브 위치, 방향 조정
    nx, ny = cx + dxs[direct], cy + dys[direct]
    if not in_range(nx,ny):
        direct = (direct + 2) % 4
    cx, cy = cx + dxs[direct], cy + dys[direct]
    cd = direct

    # 큐브 숫자조정
    arrange_cube(direct)

    # 점수 획득
    get_score(cx,cy)

    return

def arrange_cube(direct):
    f = cube[FRONT]
    d = cube[DOWN]
    r = cube[RIGHT]
    if direct == 0:
        cube[FRONT] = f
        cube[DOWN] = r
        cube[RIGHT] = 7-d
    elif direct == 1:
        cube[FRONT] = 7-d
        cube[DOWN] = f
        cube[RIGHT] = r
    elif direct == 2:
        cube[FRONT] = f
        cube[DOWN] = 7-r
        cube[RIGHT] = d
    else:
        cube[FRONT] = d
        cube[DOWN] = 7-f
        cube[RIGHT] = r
    return

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def can_go(x,y,num):
    return in_range(x,y) and not visited[x][y] and grid[x][y] == num

def get_score(x,y):
    global score
    clear_visited()
    num = grid[x][y]
    size = 1
    push(x,y)
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs,dys):
            nx, ny = x + dx, y + dy
            if can_go(nx,ny,num):
                push(nx,ny)
                size += 1

    score += num * size
    return

def push(x,y):
    visited[x][y] = True
    q.append((x,y))
    return

def clear_visited():
    for x in range(N):
        for y in range(N):
            visited[x][y] = False

def print_status():
    print("location : ",cx,cy,cd)
    print("cube : ",cube[FRONT],cube[DOWN],cube[RIGHT])
    print("score : ",score)
    print("--------------")
    return

##########################################
roll_cube(cd)
#print_status()
for i in range(M-1):
    if cube[DOWN] > grid[cx][cy]:
        cd = (cd + 1) % 4
    elif cube[DOWN] < grid[cx][cy]:
        cd = (cd - 1 + 4) % 4

    roll_cube(cd)
    #print_status()

print(score)