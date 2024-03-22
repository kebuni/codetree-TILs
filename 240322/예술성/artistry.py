from collections import deque

N = int(input())
grid = [list(map(int,input().split())) for i in range(N)]
group_grid = [[0 for j in range(N)] for i in range(N)]
group_size = [-1]
group_to_num = [-1]
visited = [[False for i in range(N)] for j in range(N)]

dxs = [-1,0,1,0]
dys = [0,1,0,-1]
q = deque()

#######################################################

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def can_go(x,y,s):
    return in_range(x,y) and not visited[x][y] and grid[x][y] == s

def get_score():

    # print("current grid-------")
    # print_grid()

    get_group_info()

    # print("group info-------")
    # print_group_grid()
    # print(group_size)
    # print(group_to_num)

    group_boundary = get_group_boundary_info()

    # print("group boundary------")
    # print_group_boundary(group_boundary)

    # gruop_boundary 가지고 점수 계산
    result = 0
    group_num = len(group_size)
    for g1 in range(1,group_num):
        for g2 in range(g1+1,group_num):
            temp_result = (group_size[g1] + group_size[g2]) * group_to_num[g1] * group_to_num[g2] * group_boundary[g1][g2]
            # print("for group",g1,g2,": ",temp_result)
            result += temp_result

    return result

def print_group_grid():
    print("group grid")
    for x in range(N):
        for y in range(N):
            print(group_grid[x][y],end=' ')
        print()
    print()
    return

def get_group_info():
    global group_size, group_to_num
    group_num = 1
    clear_visited()
    group_size = [-1]
    group_to_num = [-1]
    for x in range(N):
        for y in range(N):
            if not visited[x][y]:
                size = bfs(x,y,group_num)
                group_size.append(size)
                group_to_num.append(grid[x][y])
                group_num += 1
    return

def bfs(x,y,group_num):
    size = 1
    real_num = grid[x][y]
    push(x,y,group_num)
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs,dys):
            nx, ny = x + dx, y + dy
            if can_go(nx,ny,real_num):
                push(nx,ny,group_num)
                size += 1

    return size

def push(x,y,group_num):
    visited[x][y] = True
    group_grid[x][y] = group_num
    q.append((x,y))
    return

def clear_visited():
    for x in range(N):
        for y in range(N):
            visited[x][y] = False
            group_grid[x][y] = 0
    return

def get_group_boundary_info():
    group_num = len(group_size)
    group_boundary = [[0 for i in range(group_num)] for j in range(group_num)]
    for x in range(N):
        for y in range(N):
            cur_group = group_grid[x][y]
            for i in range(2):
                nx, ny = x + dxs[i], y + dys[i]
                # 조사하는 곳이 현재와 다른 칸, 즉 경계라면
                if in_range(nx,ny) and group_grid[nx][ny] != cur_group:
                    group_boundary[cur_group][group_grid[nx][ny]] += 1
                    group_boundary[group_grid[nx][ny]][cur_group] += 1

    return group_boundary

def rotate():
    result_grid = [[0 for i in range(N)] for j in range(N)]

    for x in range(N):
        for y in range(N):
            result_grid[N-1-y][x] = grid[x][y]

    l = N//2
    for a, b in [(0,0),(0,l+1),(l+1,0),(l+1,l+1)]:
        for x in range(l):
            for y in range(l):
                result_grid[a+y][b+(l-1-x)] = grid[a+x][b+y]

    for x in range(N):
        for y in range(N):
            grid[x][y] = result_grid[x][y]

    # print("after_rotate")
    # print_grid()

    return

def print_grid():
    print("grid")
    for x in range(N):
        for y in range(N):
            print(grid[x][y],end=' ')
        print()
    print()
    return

def print_group_boundary(group_boundary):
    print("group boundary")
    L = len(group_boundary)
    for x in range(L):
        for y in range(L):
            print(group_boundary[x][y],end=' ')
        print()
    print()
    return

#######################################################
score = 0

score += get_score()
rotate()
score += get_score()
rotate()
score += get_score()
rotate()
score += get_score()

print(score)