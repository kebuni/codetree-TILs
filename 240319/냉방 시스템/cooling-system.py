from collections import deque

dxs = [0,-1,0,1]
dys = [-1,0,1,0]

NO_WALL = 0
UP_WALL = 1
LEFT_WALL = 2
BOTH_WALL = 3

q = deque()

N, M, K = map(int,input().split())
wall_grid = [[NO_WALL for i in range(N)]for j in range(N)]
cooling_grid = [[0 for i in range(N)]for j in range(N)]
delta = [[0 for i in range(N)]for j in range(N)]
#step = [[False for i in range(N)]for j in range(N)]
office_list = []
aircon_list = []
result_cooling_grid = [[0 for i in range(N)] for j in range(N)]
for x in range(N):
    line = list(map(int,input().split()))
    for y, elem in enumerate(line):
        if elem == 0:
            continue
        if elem == 1:
            office_list.append((x,y))
        else:
            aircon_list.append((x,y,elem-2))

for i in range(M):
    x, y, s = map(int,input().split())
    wall_grid[x-1][y-1] += (s+1)

######################################################
def print_wall_grid():
    for x in range(N):
        for y in range(N):
            print(f'{wall_grid[x][y]:2}', end=' ')
        print()
    print()
    return

def print_cooling_grid():
    for x in range(N):
        for y in range(N):
            print(f'{cooling_grid[x][y]:2}',end=' ')
        print()
    print()
    return

def cooling():
    for x, y, d in aircon_list:
        clear_delta()
        cooling_one(x,y,d)
        # print("cooling for ",x,y,d)
        # print_delta()
        add_cooling_delta()
    return

def add_cooling_delta():
    for x in range(N):
        for y in range(N):
            result_cooling_grid[x][y] += delta[x][y]
    return

def add_cooling():
    for x in range(N):
        for y in range(N):
            cooling_grid[x][y] += result_cooling_grid[x][y]
    return

def cooling_one(x,y,d):
    rd = (d + 1) % 4
    ld = (d - 1 + 4) % 4
    nx, ny = x + dxs[d], y + dys[d]
    push(nx,ny,5)
    while q:
        x, y = q.popleft()
        if delta[x][y]: #아직 cooling이 퍼질 수 있다면
            # x, y로부터 앞부분으로 보내보고 가능하면 push
            nx, ny = x + dxs[d], y + dys[d]
            if can_go_for_bfs(x,y,nx,ny):
                push(nx,ny,delta[x][y]-1)
            # x, y로부터 오른쪽 앞으로 보내보고 가능하면 push
            nx, ny = x + dxs[rd], y + dys[rd]
            if can_go_for_bfs(x,y,nx,ny):
                n2x, n2y = nx + dxs[d], ny + dys[d]
                if can_go_for_bfs(nx,ny,n2x,n2y):
                    push(n2x,n2y,delta[x][y]-1)
            # x, y로부터 왼쪽 앞으로 보내보고 가능하면 push
            nx, ny = x + dxs[ld], y + dys[ld]
            if can_go_for_bfs(x,y,nx,ny):
                n2x, n2y = nx + dxs[d], ny + dys[d]
                if can_go_for_bfs(nx, ny, n2x, n2y):
                    push(n2x, n2y, delta[x][y] - 1)
    return

def push(x,y,s):
    delta[x][y] = s
    q.append((x,y))
    return

def mix():
    clear_delta()
    for x in range(N):
        for y in range(N):
            if can_go(x,y,x,y-1):
                mix_one(x,y,x,y-1)
            if can_go(x,y,x-1,y):
                mix_one(x,y,x-1,y)
    add_delta()
    return

def mix_one(x,y,nx,ny):
    diff = abs(cooling_grid[x][y] - cooling_grid[nx][ny])
    if cooling_grid[x][y] > cooling_grid[nx][ny]:
        delta[x][y] -= diff // 4
        delta[nx][ny] += diff // 4
    elif cooling_grid[x][y] < cooling_grid[nx][ny]:
        delta[x][y] += diff // 4
        delta[nx][ny] -= diff // 4
    else:
        return
    return

def decrease():
    for y in range(N):
        if cooling_grid[0][y]:
            cooling_grid[0][y] -= 1
        if cooling_grid[N-1][y]:
            cooling_grid[N-1][y] -= 1
    for x in range(1,N-1):
        if cooling_grid[x][0]:
            cooling_grid[x][0] -= 1
        if cooling_grid[x][N-1]:
            cooling_grid[x][N-1] -= 1
    return

def check_end():
    for x, y in office_list:
        if cooling_grid[x][y] < K:
            return False
    return True

def can_go(x,y,nx,ny):
    # (x,y)로부터 d 방향으로 한칸 갈 수 있는지 판단합니다.
    # mix 용입니다.
    if not in_range(nx, ny):
        return False

    if nx == x and ny == y - 1:  # 왼쪽
        if wall_grid[x][y] == LEFT_WALL or wall_grid[x][y] == BOTH_WALL:
            return False
    elif nx == x + 1 and ny == y:  # 아래쪽
        if wall_grid[nx][ny] == UP_WALL or wall_grid[nx][ny] == BOTH_WALL:
            return False
    elif nx == x and ny == y + 1:  # 오른쪽
        if wall_grid[nx][ny] == LEFT_WALL or wall_grid[nx][ny] == BOTH_WALL:
            return False
    else:  # 위쪽
        if wall_grid[x][y] == UP_WALL or wall_grid[x][y] == BOTH_WALL:
            return False

    return True

def can_go_for_bfs(x,y,nx,ny):
    if in_range(nx,ny) and delta[nx][ny]:
        return False
    return can_go(x,y,nx,ny)

def clear_delta():
    for x in range(N):
        for y in range(N):
            delta[x][y] = 0
    return

def add_delta():
    for x in range(N):
        for y in range(N):
            cooling_grid[x][y] += delta[x][y]
    return

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def print_delta():
    for x in range(N):
        for y in range(N):
            print(delta[x][y],end=' ')
        print()
    print()
    return

def print_result_cooling_grid():
    for x in range(N):
        for y in range(N):
            print(result_cooling_grid[x][y],end=' ')
        print()
    print()
    return

######################################################
ans = -1
cooling()
#print_result_cooling_grid()

for T in range(1,101):
    add_cooling()
    # print("after cooling")
    # print_cooling_grid()

    mix()
    # print("after mix")
    # print_cooling_grid()

    decrease()
    # print("after decrease")
    # print_cooling_grid()

    if check_end():
        ans = T
        break

print(ans)