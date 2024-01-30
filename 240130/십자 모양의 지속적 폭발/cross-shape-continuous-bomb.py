grid = []

########

def print_grid():
    for i in range(N):
        for j in range(N):
            print(grid[i][j],end=' ')
        print()

def find_bomb(col):
    for i in range(N):
        if grid[i][col]:
            return i
    return -1
        
def has_exploded(origin_x,origin_y,x,y,size):
    return (x == origin_x and abs(y-origin_y)<=size-1) or \
            (y == origin_y and abs(x-origin_x)<=size-1 )
    
def explode(row,col):
    global grid
    size = grid[row][col]
    for i in range(N):
        for j in range(N):
            if has_exploded(row,col,i,j,size):
                grid[i][j] = 0

def fall():
    global grid
    for j in range(N):
        temp = [0] * N
        cnt = 0
        for i in range(N-1,-1,-1):
            if grid[i][j]:
                temp[cnt] = grid[i][j]
                cnt += 1
        for i in range(N):
            grid[i][j] = temp[N-1-i]

########

N, M = map(int,input().split())

for _ in range(N):
    grid.append(list(map(int,input().split())))

for _ in range(M):
    
    bomb_col = int(input())
    
    bomb_row = find_bomb(bomb_col-1)
    #print(bomb_row)

    if bomb_row != -1:
        explode(bomb_row,bomb_col-1)
        fall()

print_grid()