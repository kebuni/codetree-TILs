grid = []
dxs = [-1,0,1,0]
dys = [0,1,0,-1]
directions = {'U':0,'R':1,'D':2,'L':3}

# 주사위 정보
cur = 6
up = 5
right = 3

##################

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def print_grid():
    for i in range(N):
        for j in range(N):
            print(grid[i][j],end=' ')
        print()

def roll(command):
    global cur,up,right,cur_x,cur_y
    nx = cur_x + dxs[directions[command]]
    ny = cur_y + dys[directions[command]]

    if not in_range(nx,ny):
        #print("can't move")
        return
    
    # 만약 in range이면

    cur_x = nx
    cur_y = ny

    if command == 'U':
        temp = cur
        cur = up
        up = 7-temp
    elif command == 'R':
        temp = cur
        cur = right
        right = 7-temp
    elif command == 'D':
        temp = cur
        cur = 7-up
        up = temp
    else:
        temp = cur
        cur = 7-right
        right = temp

    #print(cur_x,cur_y,cur,up,right)
    return 

def cal_sum():
    sum = 0
    for i in range(N):
        for j in range(N):
            sum += grid[i][j]
    return sum

##################

N, M, cur_x, cur_y = map(int,input().split())
cur_x -= 1
cur_y -= 1
for _ in range(N):
    grid.append([0 for _ in range(N)])
commands = list(input().split())

grid[cur_x][cur_y] = cur

for command in commands:
    roll(command)
    grid[cur_x][cur_y] = cur
    #print_grid()
    
print(cal_sum())