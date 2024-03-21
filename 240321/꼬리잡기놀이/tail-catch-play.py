from collections import deque

OUT_OF_GRID = 100

N, M, K = map(int,input().split())
input_grid = [list(map(int,input().split())) for i in range(N)]
path_grid = [[0 for i in range(N)] for j in range(N)]
people_grid = [[0 for i in range(N)] for j in range(N)]
step = [[-1 for i in range(N)] for j in range(N)]
visited = [[False for i in range(N)] for j in range(N)]
head = [(OUT_OF_GRID,OUT_OF_GRID) for i in range(M+1)]
tail = [(OUT_OF_GRID,OUT_OF_GRID) for i in range(M+1)]

dxs = [-1,0,1,0]
dys = [0,1,0,-1]
q = deque()

################################################

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def can_go_for_path(x,y):
    return in_range(x,y) and not visited[x][y] and input_grid[x][y]

def clear_q():
    q.clear()
    return

def clear_step():
    for i in range(N):
        for j in range(N):
            step[i][j] = -1
    return

def clear_visited():
    for i in range(N):
        for j in range(N):
            visited[i][j] = False
    return

def initialize():
    team_num = 1
    # path grid, people grid 만들기
    for x in range(N):
        for y in range(N):
            if input_grid[x][y] and not visited[x][y]:
                bfs_for_path(x,y,team_num)
                team_num += 1
    # head, tail 정보 만들기
    for x in range(N):
        for y in range(N):
            if input_grid[x][y] == 1:
                people_grid[x][y] = 1
                head[path_grid[x][y]] = (x,y)
            elif input_grid[x][y] == 3:
                people_grid[x][y] = 1
                tail[path_grid[x][y]] = (x,y)
            elif input_grid[x][y] == 2:
                people_grid[x][y] = 1
    return

def bfs_for_path(x,y,team_num):
    clear_q()
    push_for_path(x,y,team_num)
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs,dys):
            nx, ny = x + dx, y + dy
            if can_go_for_path(nx,ny):
                push_for_path(nx,ny,team_num)
    return

def push_for_path(x,y,team_num):
    path_grid[x][y] = team_num
    visited[x][y] = True
    q.append((x,y))
    return

def print_path_grid():
    for x in range(N):
        for y in range(N):
            print(path_grid[x][y],end=' ')
        print()
    print()
    return

def print_people_grid():
    for x in range(N):
        for y in range(N):
            print(people_grid[x][y],end=' ')
        print()
    print()
    return

def move():
    for i in range(1,M+1):
        hx, hy = head[i]
        tx, ty = tail[i]

        # people grid에서 head 옮기고 업데이트
        for dx, dy in zip(dxs,dys):
            nx, ny = hx + dx, hy + dy
            if in_range(nx,ny) and not people_grid[nx][ny] and path_grid[nx][ny]:
                # 격자 내고, 사람 없고, 길이면 그곳으로 헤드 옮김
                people_grid[nx][ny] = 1
                head[i] = (nx,ny)
                break

        # people grid에서 tail 옮기고 업데이트
        for dx, dy in zip(dxs,dys):
            nx, ny = tx + dx, ty + dy
            if in_range(nx,ny) and people_grid[nx][ny] and path_grid[nx][ny]:
                # 격자 내고, 사람 있고, 길이면 그곳으로 테일 옮김
                people_grid[tx][ty] = 0
                tail[i] = (nx,ny)
                break

    return

def throw_ball(turn_num):
    bx, by, bd = get_ball_pos(turn_num)
    while in_range(bx,by):
        if people_grid[bx][by]:
            get_score(bx,by)
            break
        bx, by = bx + dxs[bd], by + dys[bd]
    return

def get_score(x,y):
    global score
    # x, y에 있는 사람이 공에 맞았을 때
    # 그 사람이 몇 팀인지 보고
    team_num = path_grid[x][y]

    # 그 사람이 몇 번째 사람인지 찾아서 점수 올리고
    hx, hy = head[team_num]
    order = get_order(hx,hy,x,y)
    score += order * order

    # 그 팀의 머리와 꼬리 바꾸기
    temp = head[team_num]
    head[team_num] = tail[team_num]
    tail[team_num] = temp
    return

def get_order(hx,hy,cx,cy):
    # hx, hy로부터 사람들을 따라 갔을 때 x,y 가 몇번째 사람인지 찾습니다.
    clear_step()
    step[hx][hy] = 0
    order_q = deque()
    order_q.append((hx,hy))
    while order_q:
        x, y = order_q.popleft()
        for dx, dy in zip(dxs,dys):
            nx, ny = x + dx, y + dy
            if can_go_for_order(nx,ny):
                step[nx][ny] = step[x][y] + 1
                order_q.append((nx,ny))

    return step[cx][cy] + 1

def can_go_for_order(x,y):
    return in_range(x,y) and people_grid[x][y] and step[x][y] == -1

def get_ball_pos(turn_num):
    turn_num = turn_num % (4*N)
    q = turn_num // N
    r = turn_num % N
    if q == 0:
        return r, 0, 1
    elif q == 1:
        return N-1, r, 0
    elif q == 2:
        return N-1-r, N-1, 3
    else:
        return 0, N-1-r, 2

################################################
score = 0
initialize()

# print_path_grid()
# print_people_grid()
# print(head)
# print(tail)

for i in range(K):
    #print('--------------',i,'---------------')
    move()
    # print("after_move")
    # print_people_grid()
    # print(head)
    # print(tail)

    throw_ball(i)
    # print("after_throw_ball")
    # print_people_grid()
    # print(head)
    # print(tail)
    # print(score)

print(score)