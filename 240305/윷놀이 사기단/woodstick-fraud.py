player_nums = list(map(int,input().split()))

END = 36
ans = 0
player_loc = [0,0,0,0]

board = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
         10,13,16,19, #20 21 22 23
         20,22,24,0, #24 25 26 27
         30,28,27,26, #28 29 30 31
         25,30,35,40,0] #32 33 34 35 36

############################################
def get_next_loc(cur_loc, move_num, is_blue):
    if is_blue:
        # 여기 왔다는 건, 처음 시작 위치가 파란칸이었다는 뜻
        if cur_loc == 5:
            return get_next_loc(20, move_num, False)
        elif cur_loc == 10:
            return get_next_loc(24, move_num, False)
        else:
            return get_next_loc(28, move_num, False)
    else:

        if move_num == 0:
            return cur_loc

        # 아직 move_num 이 남아있다면?
        if cur_loc == 19:
            return get_next_loc(35, move_num - 1, False)
        elif cur_loc == 23:
            return get_next_loc(32, move_num - 1, False)
        elif cur_loc == 26:
            return get_next_loc(32, move_num - 1, False)
        elif cur_loc == 31:
            return get_next_loc(32, move_num-1, False)
        elif cur_loc == 36:
            return 36
        else:
            return get_next_loc(cur_loc+1,move_num-1,False)

def check_blue(n):
    return n == 5 or n == 10 or n == 15

def overlapped():
    return any([
        player_loc[i] == player_loc[j] and
        player_loc[i] != 0 and player_loc[i] != END
        for i in range(4)
        for j in range(i+1,4)
    ])

def find_max_score(n, current_score):
    if n == 10:
        global ans
        ans = max(ans,current_score)
        return

    for i in range(4):
        # i번째 말을 옮겨봅니다.
        if player_loc[i] == END:
            continue

        temp = player_loc[:]
        cur_loc = player_loc[i]
        next_loc = get_next_loc(cur_loc,player_nums[n],check_blue(cur_loc))
        player_loc[i] = next_loc

        if not overlapped():
            find_max_score(n+1, current_score + board[next_loc])

        for i in range(4):
            player_loc[i] = temp[i]

    return

############################################

find_max_score(0,0)
print(ans)