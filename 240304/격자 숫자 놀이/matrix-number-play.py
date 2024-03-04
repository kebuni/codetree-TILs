import sys

grid = [[0 for i in range(100)] for j in range(100)]
next_grid = [[0 for i in range(100)] for j in range(100)]
row_max, col_max = 2, 2

R, C, K = map(int, input().split())
R -= 1; C-= 1
ans = 0

for i in range(3):
    grid[i][0], grid[i][1], grid[i][2] = map(int,input().split())

##################################################

def simulate():
    if row_max >= col_max:
        play_row()
    else:
        play_col()
    return

def play_row():
    global col_max
    for x in range(row_max+1):
        dic = {}
        new_row = []
        for y in range(col_max+1):
            if grid[x][y]:
                num = grid[x][y]
                if num in dic:
                    dic[num] += 1
                else:
                    dic[num] = 1
        # 다 만들어 졌으면
        for num in dic:
            f = dic[num]
            new_row.append((f,num))

        # new_row 정렬 및 cut
        new_row.sort()
        if len(new_row) >= 50:
            new_row = new_row[:50]

        # col_max 업데이트
        col_max = max(col_max,len(new_row)*2-1)

        # next_grid에 써주기
        for idx, (f, num) in enumerate(new_row):
            next_grid[x][idx*2] = num
            next_grid[x][idx*2+1] = f

    return

def play_col():
    global row_max
    for y in range(col_max + 1):
        dic = {}
        new_col = []
        for x in range(row_max + 1):
            if grid[x][y]:
                num = grid[x][y]
                if num in dic:
                    dic[num] += 1
                else:
                    dic[num] = 1
        # 다 만들어 졌으면
        for num in dic:
            f = dic[num]
            new_col.append((f, num))

        # new_col 정렬 및 cut
        new_col.sort()
        if len(new_col) >= 50:
            new_col = new_col[:50]

        # row_max 업데이트
        row_max = max(row_max, len(new_col) * 2 - 1)

        # next_grid에 써주기
        for idx, (f, num) in enumerate(new_col):
            next_grid[idx*2][y] = num
            next_grid[idx * 2 + 1][y] = f

    return

def print_grid():
    for i in range(100):
        for j in range(100):
            #print(f'{grid[i][j]:3}',end=' ')
            print(grid[i][j],end=' ')
        print()
    print()

def clear_next_grid():
    for i in range(100):
        for j in range(100):
            next_grid[i][j] = 0

def copy_grid():
    for i in range(100):
        for j in range(100):
            grid[i][j] = next_grid[i][j]

##################################################

#print_grid()

for t in range(100):
    clear_next_grid()
    simulate()
    copy_grid()
    #print_grid()
    #print(row_max,col_max)
    #print('-----------------')
    ans += 1
    if grid[R][C] == K:
        print(ans)
        sys.exit(0)

print(-1)