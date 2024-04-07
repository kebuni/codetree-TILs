board = [0,2,4,6,8,10, # 0 1 2 3 4 5
         12,14,16,18,20, # 6 7 8 9 10
         22,24,26,28,30, # 11 12 13 14 15
         32,34,36,38, # 16 17 18 19
         13,16,19, # 20 21 22
         22,24, # 23 24
         28,27,26, # 25 26 27
         25,30,35,40,0] # 28 29 30 31 32

def get_next_pos(cur_pos, num, blue):
    for i in range(num):
        cur_pos, blue = next_pos(cur_pos, blue)
        if cur_pos == 32:
            return 32
    return cur_pos

def next_pos(cur, blue):
    if cur == 32:
        return 32, blue

    # blue 처리
    if blue and cur == 5:
        return 20, False
    if blue and cur == 10:
        return 23, False
    if blue and cur == 15:
        return 25, False

    if cur == 19:
        return 31, blue
    if cur == 22:
        return 28, blue
    if cur == 24:
        return 28, blue
    if cur == 27:
        return 28, blue

    return cur + 1, blue

def find_max_score(n,score):
    global ans, pos_list

    #print("[find_max_score]",n,score)
    #print("pos_list",pos_list)

    if n == 10:
        ans = max(ans, score)
        #print("new ans:", ans)
        return

    # 4말에 대해 이동이 가능 하다면 점수를 더하여 다음 함수를 호출합니다.
    cur_dist = dist_list[n]
    for i in range(4):
        temp_pos_list = pos_list[:]
        next_pos = get_next_pos(pos_list[i],cur_dist,get_blue(pos_list[i]))
        # print("now player",i,"in",pos_list[i],"goes",cur_dist,"times so arrive",next_pos)
        if is_valid_next_pos(next_pos):
            #print("can go to",next_pos,"and new_score",score+board[next_pos])
            #print()
            pos_list[i] = next_pos
            find_max_score(n+1,score+board[next_pos])
            pos_list = temp_pos_list

    return

def get_blue(cur_pos):
    return cur_pos == 5 or cur_pos == 10 or cur_pos == 15

def is_valid_next_pos(next_pos):
    if next_pos == 32:
        return True

    if next_pos in pos_list:
        return False
    else:
        return True

#############################
ans = 0
dist_list = list(map(int,input().split()))
pos_list = [0,0,0,0]
find_max_score(0,0)
print(ans)