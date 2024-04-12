L, N, Q = map(int,input().split())
map_grid = [list(map(int,input().split())) for i in range(L)]
grid = [[0 for i in range(L)] for j in range(L)]
player_info = [(-1,-1,-1)]
player_pos = [(-1,-1)]
hp = [-1]
involved = set()

for player_num in range(N):
    r, c, h, w, k = map(int,input().split())
    player_info.append((h,w,k))
    hp.append(k)
    player_pos.append((r-1,c-1))
    for i in range(h):
        for j in range(w):
            grid[r-1+i][c-1+j] = player_num + 1

query = [tuple(map(int,input().split())) for i in range(Q)]

dxs = [-1,0,1,0]
dys = [0,1,0,-1]

###############################################

def in_range(x,y):
    return 0<=x<L and 0<=y<L

def print_grid(A):
    for x in range(L):
        for y in range(L):
            print(A[x][y],end=' ')
        print()
    print()
    return

def alive(player_num):
    return hp[player_num] > 0

def move(d):
    # can_move가 가능해야만 호출
    # involve에 있는 player에 대해 pos를 옮겨줌
    for player_num in involved:
        x, y = player_pos[player_num]
        player_pos[player_num] = (x+dxs[d],y+dys[d])

    # pos 반영해서 업데이트
    update_grid()
    return

def update_grid():

    # 그리드 초기화
    for x in range(L):
        for y in range(L):
            grid[x][y] = 0

    # 살아 있는 플레이어에 대해 grid를 업데이트 해줍니다.
    for player_num in range(1,N+1):
        if hp[player_num] > 0:
            px, py = player_pos[player_num]
            ph, pw, pk = player_info[player_num]
            for x in range(px,px+ph):
                for y in range(py,py+pw):
                    grid[x][y] = player_num

    return

def can_move(player_num, d):
    # player_num이 d 방향으로 갈 수 있는지 판정
    # involved에 player_num 추가
    involved.add(player_num)
    px, py = player_pos[player_num]
    ph, pw, pk = player_info[player_num]

    # 기사로부터 d방향에 접해있는 모든 칸에 대해 갈 수 있어야 합니다.
    if d == 0: #위로 갈 경우
        for y in range(py,py+pw):
            if not can_move_one(px,y,d):
                return False
    elif d == 1: #오른쪽으로 갈 경우
        for x in range(px,px+ph):
            if not can_move_one(x,py+pw-1,d):
                return False
    elif d == 2: #아래로 갈 경우
        for y in range(py,py+pw):
            if not can_move_one(px+ph-1,y,d):
                return False
    else: # 왼쪽으로 갈 경우
        for x in range(px,px+ph):
            if not can_move_one(x,py,d):
                return False

    # 모든 칸에 대해 통과했다면 player_num은 이동이 가능합니다.
    return True

def can_move_one(x,y,d):
    # x,y칸이 d로 갈 수 있는지 판정
    nx, ny = x + dxs[d], y + dys[d]

    # 범위 밖이면 갈 수 없습니다.
    if not in_range(nx,ny):
        return False

    # 범위 안이고 옆칸에 벽이 있다면
    if map_grid[nx][ny] == 2:
        return False

    # 범위 안이고 옆칸에 벽이 없다면
    # 옆 칸에 기사가 있다면, 그 기사가 갈 수 있어야 합니다.
    # 다만 중복 계산을 줄이기 위해 involved에 있다면 pass합니다
    if grid[nx][ny] != 0:
        if grid[nx][ny] in involved:
            return True
        else:
            return can_move(grid[nx][ny],d)

    # 범위 안이고 옆칸에 벽도 없고 기사도 없다면 갈 수 있습니다.
    return True

def update_hp(player_num):
    # involved 에 있는 player들 중에서 player_num이 아닌 애들에 대해
    # 함정의 수만큼 데미지 입기
    check_list = set()

    for x in range(L):
        for y in range(L):
            # 함정이라면
            if map_grid[x][y] == 1:
                # 함정에 기사가 있고 그 기사가 명령 받은 기사가 아니라면
                if grid[x][y] > 0 and grid[x][y] in involved and grid[x][y] != player_num:
                    hp[grid[x][y]] -= 1
                    check_list.add(grid[x][y])

    # 이번 판에 참여한 player 중에서...
    # 만약 hp가 0 이하가 됐으면
    # hp 업데이트해주고 grid에서 지워주기
    for player_num in check_list:
        if hp[player_num] <= 0:
            hp[player_num] = 0
            px, py = player_pos[player_num]
            ph, pw, pk = player_info[player_num]
            for x in range(px, px + ph):
                for y in range(py, py + pw):
                    grid[x][y] = 0

    return

def print_ans():
    ans = 0
    for player_num in range(1,N+1):
        if hp[player_num] > 0:
            ans += (player_info[player_num][2] - hp[player_num])
    print(ans)
    return

###############################################

# print("initailize")
# print_grid(grid)
# print(player_info)
# print(player_pos)
# print(hp)

for player_num, direct in query:
    # print('============================================')
    # print("player_num:",player_num,"direct",direct)
    if alive(player_num):

        # print("player",player_num,"alive")

        possible = can_move(player_num, direct)
        # print("possible:",possible)
        # print("involved",involved)

        if possible:

            move(direct)
            # print("after move:")
            # print_grid(grid)
            # print(player_pos)

            update_hp(player_num)
            # print("after update hp")
            # print_grid(grid)
            # print(hp)

        involved.clear()

# print("done============")
print_ans()