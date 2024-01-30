grid = []

#######################
def print_grid():
    for i in range(N):
        for j in range(N):
            print(grid[i][j],end=' ')
        print()

def find_end_index(row,col,num):
    result = row
    for i in range(row,-1,-1):
        if grid[i][col] == num:
            result = i
        if grid[i][col] != num:
            break
    return result

def explode():
    global grid

    while True:

        exploded = False

        for j in range(N):
            for i in range(N-1,-1,-1):
                if grid[i][j]:
                    end = find_end_index(i,j,grid[i][j])
                    #print(i,end)
                    if i - end >= M-1:
                        exploded = True
                        for k in range(end,i+1):
                            grid[k][j] = 0

        fall()

        if not exploded:
            break

def rotate():
    global grid
    next_grid = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            next_grid[i][j] = grid[N-1-j][i]
    for i in range(N):
        for j in range(N):
            grid[i][j] = next_grid[i][j]

def fall():
    global grid
    next_grid = [[0]*N for _ in range(N)]
    for j in range(N):
        cnt = N-1
        for i in range(N-1,-1,-1):
            if grid[i][j]:
                next_grid[cnt][j] = grid[i][j]
                cnt -= 1

    for i in range(N):
        for j in range(N):
            grid[i][j] = next_grid[i][j]

def remain_bombs():
    cnt = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j]:
                cnt += 1
    return cnt

#######################

N, M, K = map(int,input().split())

for _ in range(N):
    grid.append(list(map(int,input().split())))

for i in range(K):
    # print(i,"#####################")
    explode()
    # print_grid()
    # print('---------------')
    rotate()
    # print_grid()
    # print('---------------')
    fall()
    # print_grid()
    # print('---------------')

explode()
#print_grid()
#print('---------------')
print(remain_bombs())