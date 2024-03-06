BLOCK = 1
NO_BLOCK = 0

K = int(input())
blocks = [tuple(map(int,input().split())) for i in range(K)]
red_blocks = []
for t, x, y in blocks:
    if t == 1:
        red_blocks.append((1,y,3-x))
    elif t == 2:
        red_blocks.append((3,y,3-x))
    else:
        red_blocks.append((2,y,3- x -1))


yellow_grid = [[0 for i in range(4)] for j in range(6)]
yellow_floors = [5,5,5,5]

score = 0
remain_tile_num = 0

##########################################

def drop_block(t,x,y):
    if t==1:
        drop_block_type1(x,y)
    elif t==2:
        drop_block_type2(x,y)
    else:
        drop_block_type3(x,y)
    return

def get_score():
    global score
    # 꽉 채워진 열이나 행을 표시한후
    # 한번에 제거합니다
    # 점수를 업데이트합니다
    # floor도 새로 업데이트 해야합니다.

    yellow_complete = [False, False, False, False, False, False]
    yellow_grid_next = [[0 for i in range(4)] for j in range(6)]

    # yellow part
    complete_num = 0
    for x in range(2,6):
        if check_row_complete(x):
            yellow_complete[x] = True
            complete_num += 1

    if complete_num == 0:
        return

    # next 배열에 옮겨줍니다
    next_x = 5
    for x in range(5,-1,-1):
        if not yellow_complete[x]:
            for y in range(4):
                yellow_grid_next[next_x][y] = yellow_grid[x][y]
            next_x -= 1

    for x in range(6):
        for y in range(4):
            yellow_grid[x][y] = yellow_grid_next[x][y]

    # 점수를 추가합니다
    score += complete_num

    # floor 업데이트
    update_yellow_floor()

    return

def check_row_complete(x):
    for y in range(4):
        if not yellow_grid[x][y]:
            return False
    return True

def update_yellow_floor():
    for y in range(4):
        yellow_floors[y] = 5
        for x in range(6):
            if yellow_grid[x][y]:
                yellow_floors[y] = x - 1
                break
    return

def push_block():
    # 튀어나온 양을 조사한후
    # 그만큼 밀어야 합니다
    # floor도 새로 업데이트 해야합니다.

    push_num = 0
    for y in range(4):
        if yellow_grid[1][y]:
            push_num = 1
    for y in range(4):
        if yellow_grid[0][y]:
            push_num = 2

    if push_num == 0:
        return

    for x in range(5,1,-1):
        for y in range(4):
            yellow_grid[x][y] = yellow_grid[x-push_num][y]

    for x in range(2):
        for y in range(4):
            yellow_grid[x][y] = 0

    update_yellow_floor()

    return

def drop_block_type1(x,y):
    # floor에 블록을 떨어트리고 floor를 advance하면 됩니다.

    # yellow part
    yellow_floor = yellow_floors[y]
    yellow_grid[yellow_floor][y] = BLOCK
    update_yellow_floor()

    return

def drop_block_type2(x,y):
    # yellow part : 더 높이 있는 floor에 놔야합니다.
    yellow_floor = min(yellow_floors[y], yellow_floors[y+1])
    yellow_grid[yellow_floor][y] = BLOCK
    yellow_grid[yellow_floor][y+1] = BLOCK

    update_yellow_floor()

    return

def drop_block_type3(x,y):
    # yellow part
    yellow_floor = yellow_floors[y]
    for i in range(2):
        yellow_grid[yellow_floor-i][y] = BLOCK
    update_yellow_floor()

    return

def print_grids():
    for i in range(6):
        for j in range(4):
            print(yellow_grid[i][j],end=' ')
        print()
    print()
    for i in range(4):
        print(yellow_floors[i],end=' ')
    print()
    print()

def get_remain():
    sum = 0
    for x in range(2,6):
        for y in range(4):
            sum += yellow_grid[x][y]
    return sum

def clear_yellow_grid():
    for x in range(6):
        for y in range(4):
            yellow_grid[x][y] = 0
    for y in range(4):
        yellow_floors[y] = 5

##########################################

for t, x, y in blocks:
    #print(t,x,y)
    drop_block(t,x,y)
    get_score()
    push_block()
    #print_grids()

yellow_score = score
score = 0
yellow_remain = get_remain()
clear_yellow_grid()
# print(yellow_score,yellow_remain)
# print("===================================")

for t, x, y in red_blocks:
    #print(t, x, y)
    drop_block(t,x,y)
    get_score()
    push_block()
    #print_grids()

red_score = score
red_remain = get_remain()
# print(red_score,red_remain)
# print("===================================")

print(yellow_score + red_score)
print(yellow_remain + red_remain)