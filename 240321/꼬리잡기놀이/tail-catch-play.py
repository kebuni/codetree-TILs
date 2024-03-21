from collections import deque

dxs = [0,-1,0,1]
dys = [1,0,-1,0]

N, M, K = map(int,input().split())
input_grid = [list(map(int,input().split())) for i in range(N)]
path_grid = [[0 for i in range(N)] for j in range(N)]
people_grid = [[0 for i in range(N)] for j in range(N)]
visited = [[False for i in range(N)] for j in range(N)]
line = [deque() for i in range(M+1)]
tail = [0 for i in range(M+1)]

###############################################

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def can_go(x,y):
    return in_range(x,y) and not visited[x][y] and input_grid[x][y]

def initialize():
    team_num = 1
    for x in range(N):
        for y in range(N):
            if input_grid[x][y] == 1:
                line[team_num].append((x,y))
                dfs(x,y,team_num)
                team_num += 1

    update_people_grid()
    return

def dfs(x,y,idx):
    visited[x][y] = True
    path_grid[x][y] = idx
    for dx, dy in zip(dxs,dys):
        nx, ny = x + dx, y + dy
        if not can_go(nx,ny):
            continue
        if len(line[idx]) == 1 and input_grid[nx][ny] != 2:
            continue
        line[idx].append((nx,ny))
        if input_grid[nx][ny] == 3:
            tail[idx] = len(line[idx])
        dfs(nx,ny,idx)
    return

def update_people_grid():
    clear_people_grid()
    for team in range(1,M+1):
        for i in range(tail[team]):
            x, y = line[team][i]
            if i == 0:
                people_grid[x][y] = 1
            elif i == tail[team]-1:
                people_grid[x][y] = 3
            else:
                people_grid[x][y] = 2

    return

def move():
    for team in range(1,M+1):
        last = line[team].pop()
        line[team].appendleft(last)
    update_people_grid()
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
    team = path_grid[x][y]
    order = get_order(team,x,y)
    score += order * order
    reverse(team)
    update_people_grid()

    return

def get_order(team,x,y):
    for i in range(tail[team]):
        if line[team][i] == (x,y):
            return i+1
    print("error")
    return 0

def reverse(team):
    new_line = deque()
    for i in range(tail[team]-1,-1,-1):
        new_line.append(line[team][i])
    for i in range(len(line[team])-1,tail[team]-1,-1):
        new_line.append(line[team][i])
    line[team].clear()
    for elem in new_line:
        line[team].append(elem)
    return

def get_ball_pos(turn_num):
    turn_num = turn_num % (4*N)
    q = turn_num // N
    r = turn_num % N
    if q == 0:
        return r, 0,q
    elif q == 1:
        return N-1, r, q
    elif q == 2:
        return N-1-r, N-1, q
    else:
        return 0, N-1-r, q

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

def clear_people_grid():
    for x in range(N):
        for y in range(N):
            people_grid[x][y] = 0
    return

###############################################
score = 0
initialize()
# print_path_grid()
# print_people_grid()
# for i in range(1,M+1):
#     print("team",i,line[i])
# for i in range(1,M+1):
#     print("team tail",i,tail[i])

for i in range(K):
    move()
    # print("after move")
    # print_people_grid()
    # for t in range(1, M + 1):
    #     print("team", t, line[t])
    # for t in range(1, M + 1):
    #     print("team tail", t, tail[t])

    throw_ball(i)
    # print("after throw ball")
    # print_people_grid()
    # for t in range(1, M + 1):
    #     print("team", t, line[t])
    # for t in range(1, M + 1):
    #     print("team tail", t, tail[t])

print(score)