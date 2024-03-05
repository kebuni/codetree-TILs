N, M, Q = map(int,input().split())
grid = [[0 for i in range(M+1)]]
query = []
for i in range(N):
    grid.append([0] + list(map(int,input().split())))
for i in range(Q):
    query.append(tuple(map(int,input().split())))
del_grid = [[False for i in range(M+1)] for j in range(N+1)]

num = N*M

########################################################

def print_grid():
    for i in range(N+1):
        for j in range(M+1):
            print(grid[i][j],end=' ')
        print()
    print()

def get_sum():
    sum = 0
    for i in range(N + 1):
        for j in range(M + 1):
            sum += grid[i][j]
    return sum

def rotate(x,d,k):
    k = k % M
    for i in range(1,N+1):
        if i % x == 0:

            # print("now rotating:",i)
            # 이 판을 d방향 k만큼 회전시킵시다.
            new_row = grid[i][1:M+1]

            # 시계방향 -> 뒤에서 떼서 붙이기
            if d == 0:
                part = new_row[-k:]
                new_row = new_row[:-k]
                new_row = part + new_row
            else:
                part = new_row[:k]
                new_row = new_row[k:]
                new_row = new_row + part

            for y in range(1,M+1):
                grid[i][y] = new_row[y-1]

    return

def check_delete():
    global num
    result = True
    clear_del_grid()

    dxs = [-1,0,1,0]
    dys = [0,1,0,-1]

    for x in range(1,N+1):
        if grid[x][0] == grid[x][N] and grid[x][0] != 0:
            del_grid[x][0] = del_grid[x][N] = True

    for x in range(1,N+1):
        for y in range(1,M+1):
            for dx, dy in zip(dxs,dys):
                nx, ny = x + dx, y + dy
                if check_range(nx,ny):
                    if grid[x][y] == grid[nx][ny] and grid[x][y] != 0:
                        del_grid[x][y] = del_grid[nx][ny] = True

    for x in range(1,N+1):
        for y in range(1,M+1):
            if del_grid[x][y]:
                result = False
                grid[x][y] = 0
                num -= 1

    return result

def normalize():
    if num>0:
        avg = get_sum() // num
        for x in range(1,N+1):
            for y in range(1,M+1):
                if grid[x][y] > avg:
                    grid[x][y] -= 1
                elif grid[x][y] < avg:
                    grid[x][y] += 1
    return

def clear_del_grid():
    for i in range(N+1):
        for j in range(M+1):
            del_grid[i][j] = False
    return

def check_range(x,y):
    return 0<x<N and 0<y<M

########################################################

for x, d, k in query:
    rotate(x,d,k)
    if check_delete():
        #print('check!')
        normalize()

    #print_grid()

print(get_sum())