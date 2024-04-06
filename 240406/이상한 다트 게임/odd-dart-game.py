from collections import deque
N, M, Q = map(int,input().split())
grid = [list(map(int,input().split())) for i in range(N)]
query = [tuple(map(int,input().split())) for i in range(Q)]
next_grid = [[0 for j in range(M)] for i in range(N)]
visited = [[False for j in range(M)] for i in range(N)]

dxs = [-1,0,1,0]
dys = [0,1,0,-1]
q = deque()

num = N*M
###########################################
def in_range(x,y):
    return 0<=x<N and 0<=y<M

def can_go(x,y,s):
    return in_range(x,y) and not visited[x][y] and grid[x][y] == s

def rotate(type,direct,k):
    for row in range(N):
        if (row+1) % type == 0:
            rotate_one(row,direct,k)
    return

def rotate_one(row,direct,k):
    temp = grid[row][:]
    if direct == 0:
        for i in range(M):
            grid[row][i] = temp[(M-k+i) % M]
    else:
        for i in range(M):
            grid[row][i] = temp[(k+i) % M]
    return

def remove_neigbor_num():
    removed = False
    clear_visited_and_next_grid()

    for x in range(N):
        for y in range(M):
            if grid[x][y]:
                if not visited[x][y]:
                    temp = bfs(x,y,grid[x][y])
                    if temp:
                        removed = True

    copy_grid()
    return removed

def push(x,y):
    visited[x][y] = True
    q.append((x,y))
    return

def bfs(x,y,cur_num):
    push(x,y)
    size = 1
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs,dys):
            nx, ny = x + dx, (y + dy + M) % M
            if can_go(nx,ny,cur_num):
                push(nx,ny)
                size += 1

    # 탐색이 끝났습니다. 만약 인접한 숫자가 없는 칸이면 next에 넣어줍니다.
    if size == 1:
        next_grid[x][y] = cur_num
        return False
    else:
        return True

def clear_visited_and_next_grid():
    for x in range(N):
        for y in range(M):
            visited[x][y] = False
            next_grid[x][y] = 0
    return

def copy_grid():
    global num
    num = 0
    for x in range(N):
        for y in range(M):
            grid[x][y] = next_grid[x][y]
            if next_grid[x][y]:
                num += 1
    return

def normalize():
    if num == 0:
        return
    total_sum = get_total()
    avg = total_sum // num
    # print("avg:",avg)
    for x in range(N):
        for y in range(M):
            if grid[x][y]:
                if grid[x][y] > avg:
                    grid[x][y] -= 1
                elif grid[x][y] < avg:
                    grid[x][y] += 1
    return

def get_total():
    return sum([grid[x][y] for x in range(N) for y in range(M)])

def print_grid():
    for x in range(N):
        for y in range(M):
            print(grid[x][y],end=' ')
        print()
    print()

###########################################
for type, direct, k in query:

    rotate(type,direct,k)
    # print("after rotate",type,direct,k)
    # print_grid()

    removed = remove_neigbor_num()
    # print("after remove")
    # print_grid()
    # print("removed:",removed)
    # print("num:",num)

    if not removed:
        # print("not removed so normalize")
        normalize()
        # print_grid()

print(get_total())