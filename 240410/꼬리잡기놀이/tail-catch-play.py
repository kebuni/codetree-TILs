from collections import deque

N, M, K = map(int,input().split())
first_grid = [list(map(int,input().split())) for i in range(N)]

grid = [[-1 for i in range(N)] for j in range(N)]
team_grid = [[-1 for i in range(N)] for j in range(N)]
path = [deque() for i in range(M)]
tail = [0 for i in range(M)]
visited = [[False for i in range(N)] for j in range(N)]

dxs = [0,-1,0,1]
dys = [1,0,-1,0]
#############################################
def in_range(x,y):
    return 0<=x<N and 0<=y<N

def initialize():
    # 초기 정보를 보고 path, tail, team grid를 만듭니다.
    team_num = 0
    for x in range(N):
        for y in range(N):
            if first_grid[x][y] == 1:
                # dfs 수행
                visited[x][y] = True
                team_grid[x][y] = team_num
                path[team_num].append((x,y))

                for dx, dy in zip(dxs,dys):
                    nx, ny = x + dx, y + dy
                    if in_range(nx,ny) and first_grid[nx][ny] == 2:
                        dfs(nx,ny,x,y,team_num,1)
                        break

                team_num += 1

    # update_grid()를 만들어 grid를 완성합니다.
    update_grid()
    return

def dfs(cur_x, cur_y, first_x, first_y, team_num, num):
    if (cur_x, cur_y) == (first_x, first_y):
        return

    visited[cur_x][cur_y] = True
    team_grid[cur_x][cur_y] = team_num
    path[team_num].append((cur_x,cur_y))

    if first_grid[cur_x][cur_y] == 3:
        tail[team_num] = num

    for dx, dy in zip(dxs,dys):
        nx, ny = cur_x + dx, cur_y + dy
        if in_range(nx,ny) and not visited[nx][ny] and first_grid[nx][ny]:
            dfs(nx,ny,first_x,first_y,team_num,num+1)

    return

def move_all():
    for team_num in range(M):
        temp = path[team_num].pop()
        path[team_num].appendleft(temp)

    update_grid()
    return

def throw_ball(round_num):
    team_num, order = -1, -1

    # 공의 시작점과 방향을 구합니다.
    round_num = round_num % (4*N)
    d = round_num // N
    i = round_num % N
    if d == 0:
        y = 0
        x = i
    elif d == 1:
        x = N-1
        y = i
    elif d == 2:
        y = N-1
        x = N-1-i
    else:
        x = 0
        y = N-1-i

    # 공을 던져 맞는 사람이 있으면 team 번호와 order를 대입하여 리턴합니다.
    while in_range(x,y):
        if grid[x][y] > 0:
            team_num = team_grid[x][y]
            order = grid[x][y]
            break
        x = x + dxs[d]
        y = y + dys[d]

    return team_num, order

def get_score(team_num, order):
    global ans
    if team_num == -1:
        return

    ans += order**2

    # team_num의 순서를 뒤집습니다.
    tail_num = tail[team_num]
    temp_path = deque()
    for i in range(tail_num,-1,-1):
        temp_path.append(path[team_num][i])
    for i in range(len(path[team_num])-1,tail_num,-1):
        temp_path.append(path[team_num][i])

    #path[team_num] = temp_path[:]
    path[team_num].clear()
    for elem in temp_path:
        path[team_num].append(elem)

    # 새로 반영한 그리드를 업데이트합니다.
    update_grid()

    return

def update_grid():
    # path를 보고 grid를 그립니다.
    for x in range(N):
        for y in range(N):
            grid[x][y] = -1

    for team_num in range(M):
        for i in range(len(path[team_num])):
            x, y = path[team_num][i]
            if i <= tail[team_num]:
                grid[x][y] = i+1
            else:
                grid[x][y] = 0
    return

def print_grid(A):
    for x in range(N):
        for y in range(N):
            print(f'{A[x][y]:2}',end=' ')
        print()
    print()

#############################################
ans = 0
initialize()

# print("after initialize")
# print_grid(grid)
# print_grid(team_grid)
# print(path)
# print(tail)

for round_num in range(K):
    # print("round",round_num,"-------------------------------")

    move_all()
    # print("after move all")
    # print_grid(grid)
    # print(path)
    # print(tail)

    team_num, order = throw_ball(round_num)
    # print("team_num, order:",team_num, order)

    get_score(team_num, order)
    # print("after get score")
    # print_grid(grid)
    # print(path)
    # print(tail)
    # print("score:",ans)

print(ans)