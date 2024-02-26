EAST = 0
WEST = 1
NORTH = 2
SOUTH = 3

dxs = [0,0,-1,1]
dys = [1,-1,0,0]

N, M, cx, cy, K = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
commands = list(map(lambda x: int(x)-1,input().split()))

cube = (6,2,3)
cube_num = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

#################

def move(direct):
    global cube,cx,cy
    nx = cx + dxs[direct]
    ny = cy + dys[direct]

    # 이동하고자 하는곳이 범위 안이라면
    if in_range(nx,ny):
        cx = nx
        cy = ny

        d,f,r = cube
        if direct == EAST:
            cube = (r,f,7-d)
        elif direct == WEST:
            cube = (7-r,f,d)
        elif direct == NORTH:
            cube = (7-f,d,r)
        else:
            cube = (f,7-d,r)

        return True
    else:
        return False

def copy_num():
    global cube_num, grid
    d,f,r = cube
    if grid[cx][cy] == 0:
        grid[cx][cy] = d
    else:
        cube_num[d] = grid[cx][cy]
        grid[cx][cy] = 0
    return

def print_upper():
    d,f,r = cube
    print(cube_num[7-d])
    return

def in_range(x,y):
    return 0<=x<N and 0<=y<M

#################
# print(cube)
# print(cube_num)

for command in commands:
    moved = move(command)
    if moved:
        copy_num()
    if moved:
        print_upper()

    # print(cube)
    # print(cube_num)