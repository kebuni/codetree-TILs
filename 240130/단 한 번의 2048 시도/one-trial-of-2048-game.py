grid = []
directs = {'U':0, 'R':1, 'D':2, 'L':3}

##########

def rotate(direct):
    global grid

    temp = [[-1]*4 for _ in range(4)]
    if direct == 0:
        for i in range(4):
            for j in range(4):
                temp[i][j] = grid[3-i][3-j]
    elif direct == 1:
        for i in range(4):
            for j in range(4):
                temp[i][j] = grid[3-j][i]
    elif direct == 3:
        for i in range(4):
            for j in range(4):
                temp[i][j] = grid[j][3-i]
    else:
        return
    
    grid = temp

def process():

    for j in range(4):
        for i in range(2,-1,-1):
            if grid[i][j] == grid[i+1][j]:
                grid[i][j] = 0
                grid[i+1][j] = 2 * grid[i+1][j]

    return

def fall():
    global grid
    for j in range(4):
        temp = [0]*4
        cnt = 0
        for i in range(3,-1,-1):
            if grid[i][j]:
                temp[cnt] = grid[i][j]
                cnt += 1
        for i in range(4):
            grid[3-i][j] = temp[i]

def print_grid():
    for i in range(4):
        for j in range(4):
            print(grid[i][j],end=' ')
        print()

##########

for i in range(4):
    grid.append(list(map(int,input().split())))

direct = input()

rotate(directs[direct])
fall()
process()
fall()
if direct == 'D' or direct == 'U':
    rotate(directs[direct])
else:
    rotate((directs[(direct)]+2)%4)
print_grid()