NORTH = 0
SOUTH = 1
CW = 1
CCW = -1

chairs = []
for i in range(4):
    chairs.append(list(map(int,input())))

commands = []
rotate_list = [0 for i in range(4)]

K = int(input())
for i in range(K):
    commands.append(tuple(map(int,input().split())))

####################################################

def output_ans():
    sum = 0
    for i in range(4):
        sum += chairs[i][0] * 2**i
    print(sum)
    return

def simulate(c,d):
    global rotate_list
    rotate_list[c] = d
    check_right(c)
    check_left(c)

    #돌아가야 할 의자를 다 체크했으면
    rotate()
    return

def check_right(c):
    global rotate_list
    # c가 돌아간다고 했을 때, c+1도 돌아가는가
    if c+1 <= 3:
        if chairs[c][2] != chairs[c+1][6]:
            rotate_list[c+1] = -rotate_list[c]
            check_right(c+1)
    return

def check_left(c):
    global rotate_list
    # c가 돌아간다고 했을 때, c-1도 돌아가는가
    if c - 1 >= 0:
        if chairs[c][6] != chairs[c - 1][2]:
            rotate_list[c - 1] = -rotate_list[c]
            check_left(c-1)
    return

def clear_rotate_list():
    global rotate_list
    rotate_list = [0,0,0,0]
    return

def rotate():
    for i in range(4):
        if rotate_list[i] == CW:
            rotate_cw(i)
        elif rotate_list[i] == CCW:
            rotate_ccw(i)
    return

def rotate_cw(idx):
    temp = chairs[idx][7]
    for i in range(7,0,-1):
        chairs[idx][i] = chairs[idx][i-1]
    chairs[idx][0] = temp
    return

def rotate_ccw(idx):
    temp = chairs[idx][0]
    for i in range(0, 7):
        chairs[idx][i] = chairs[idx][i + 1]
    chairs[idx][7] = temp
    return

####################################################

for c, d in commands:
    clear_rotate_list()
    simulate(c-1,d)

#print(chairs)
output_ans()