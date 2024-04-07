K = int(input())
grid = [[0 for i in range(4)] for j in range(6)]
next_grid = [[0 for i in range(4)] for j in range(6)]
yellow_block_list = [tuple(map(int,input().split())) for i in range(K)]
red_block_list = []
for t, x, y in yellow_block_list:
    nt = t
    if nt == 2 or nt == 3:
        nt = 5 - nt
    nx = y
    ny = 3 - x
    if nt == 2:
        ny -= 1
    red_block_list.append((nt,nx,ny))

floor = [5,5,5,5]
###############################################

def drop_block(t,x,y):
    block_floor = 100
    if t == 2:
        block_floor = min(floor[y],floor[y+1])
    else:
        block_floor = floor[y]

    if t == 1:
        grid[block_floor][y] = 1
    elif t == 2:
        grid[block_floor][y] = grid[block_floor][y+1] = 1
    else:
        grid[block_floor][y] = grid[block_floor-1][y] = 1

    update_floor()
    return

def get_score():
    line_to_delete = []
    for x in range(5,1,-1):
        if is_full(x):
            line_to_delete.append(x)
    delete_line(line_to_delete,True)
    return

def decrease():
    if not is_empty(0):
        delete_line([4,5],False)
        return
    if not is_empty(1):
        delete_line([5],False)
        return
    return

def is_empty(row):
    for y in range(4):
        if grid[row][y] == 1:
            return False
    return True

def is_full(row):
    for y in range(4):
        if grid[row][y] == 0:
            return False
    return True

def get_remain():
    return sum([grid[x][y] for x in range(6) for y in range(4)])

def delete_line(lines, for_score):
    global score
    # lines에 해당하는 줄을 지우고 아래로 내립니다.
    if not lines:
        return

    clear_next_grid()
    cur_floor = 5
    for x in range(5,-1,-1):
        if x not in lines:
            for y in range(4):
                next_grid[cur_floor][y] = grid[x][y]
            cur_floor -= 1
    copy_next_grid()
    # floor 를 업데이트 합니다.
    update_floor()
    # 만약 for_score라면 지운 줄만큼 score에 추가합니다.
    if for_score:
        score += len(lines)
    return

def clear_next_grid():
    for x in range(6):
        for y in range(4):
            next_grid[x][y] = 0
    return

def copy_next_grid():
    for x in range(6):
        for y in range(4):
            grid[x][y] = next_grid[x][y]
    return

def clear_grid():
    for x in range(6):
        for y in range(4):
            grid[x][y] = 0
    return

def update_floor():
    for y in range(4):
        for x in range(6):
            floor[y] = 5
            if grid[x][y]:
                floor[y] = x-1
                break

def print_status():
    for x in range(6):
        for y in range(4):
            print(grid[x][y],end=' ')
        print()
    print()
    for y in range(4):
        print(floor[y],end=' ')
    print()
    print("score :",score)
    print()
###############################################
score = 0
yellow_left = 0
red_left = 0
for t, x, y in yellow_block_list:

    drop_block(t, x, y)
    # print("after drop block",t,x,y)
    # print_status()

    get_score()
    # print("after get score")
    # print_status()

    decrease()
    # print("after decrease")
    # print_status()

yellow_left = get_remain()
clear_grid()
floor = [5,5,5,5]

for t, x, y in red_block_list:

    drop_block(t,x,y)
    # print("after drop block",t,x,y)
    # print_status()

    get_score()
    # print("after get score")
    # print_status()

    decrease()
    # print("after decrease")
    # print_status()

red_left = get_remain()
print(score)
print(yellow_left + red_left)