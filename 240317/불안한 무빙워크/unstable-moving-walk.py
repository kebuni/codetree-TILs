N, K = map(int,input().split())
moving_walk = list(map(int,input().split()))
people_loc = [0 for i in range(N)]

############################

def rotate():
    temp = moving_walk[2*N-1]
    for i in range(2*N-1,0,-1):
        moving_walk[i] = moving_walk[i-1]
    moving_walk[0] = temp

    for i in range(N-1,0,-1):
        people_loc[i] = people_loc[i-1]
    people_loc[0] = 0
    people_loc[N-1] = 0

    return

def move_people():
    for i in range(N-2,-1,-1):
        #만약 현재 칸에 사람이 있다면
        if people_loc[i] == 1:
            #만약 다음 칸에 사람이 없고 다음칸 내구도가 0이 아니면
            if not people_loc[i+1] and moving_walk[i+1]:
                #다음칸 사람추가, 다음칸 내구도 하락, 현재칸 사람 삭제
                people_loc[i+1] = 1
                moving_walk[i+1] -= 1
                people_loc[i] = 0

    # 마지막 사람 제거
    people_loc[N-1] = 0
    return

def add_person():
    if not people_loc[0] and moving_walk[0]:
        people_loc[0] = 1
        moving_walk[0] -= 1
    return

def check_end():
    zero_stability_num = 0
    for elem in moving_walk:
        if elem == 0:
            zero_stability_num += 1
    if zero_stability_num >= K:
        return True
    else:
        return False

def print_status():
    for i in range(N):
        print(people_loc[i],end=' ')
    print()
    for i in range(N):
        print(moving_walk[i],end=' ')
    print()
    for i in range(N,2*N):
        print(moving_walk[i],end=' ')
    print()
    print('==============')
    return

############################

T = 1
while True:
    #print('#########',T,'#########')
    rotate()
    #print_status()
    move_people()
    #print_status()
    add_person()
    #print_status()
    if check_end():
        break
    T += 1

print(T)