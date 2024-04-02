dxs = [-1,0,1,0]
dys = [0,1,0,-1]

OUT_OF_GRID = (1000000,1000000)

N, M, Q = map(int,input().split())
map_grid = [list(map(int,input().split())) for i in range(N)]
knight_grid = [[0 for i in range(N)] for j in range(N) ]
next_knight_grid = [[0 for i in range(N)] for j in range(N) ]
damage = [0 for i in range(M+1)]
hp = [0 for i in range(M+1)]
pos = [OUT_OF_GRID for i in range(M+1)]
shield = [OUT_OF_GRID for i in range(M+1)]
for i in range(1,M+1):
    r, c, h, w, k = map(int,input().split())
    for x in range(h):
        for y in range(w):
            knight_grid[r-1+x][c-1+y] = i
    hp[i] = k
    shield[i] = (h,w)
    pos[i] = (r-1,c-1)

q_list = [tuple(map(int,input().split())) for i in range(Q)]
involved = set()

##############################################

def print_grid(grid):
    for x in range(N):
        for y in range(N):
            print(grid[x][y],end=' ')
        print()
    print()

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def try_move(idx, direct):
    moved = False

    if hp[idx] <= 0:
        return False

    involved.clear()
    if can_move(idx, direct):
        actual_move(direct)
        return True
    else:
        return False

def actual_move(direct):
    clear_next_knight_grid()

    for moved_knight in involved:
        x, y = pos[moved_knight]
        nx, ny = x + dxs[direct], y + dys[direct]
        pos[moved_knight] = (nx,ny)

    for x in range(N):
        for y in range(N):
            if knight_grid[x][y]:
                cur = knight_grid[x][y]
                if cur in involved:
                    nx, ny = x + dxs[direct], y + dys[direct]
                    next_knight_grid[nx][ny] = cur
                else:
                    next_knight_grid[x][y] = cur

    copy_knight_grid()
    return

def clear_next_knight_grid():
    for x in range(N):
        for y in range(N):
            next_knight_grid[x][y] = 0
    return

def copy_knight_grid():
    for x in range(N):
        for y in range(N):
            knight_grid[x][y] = next_knight_grid[x][y]
    return

def can_move(idx, direct):

    if idx == 0:
        return

    involved.add(idx)
    # print("check can move",idx,direct)

    # 위치 정보를 가져옵니다.
    r, c = pos[idx]
    h, w = shield[idx]
    check_list = []

    if direct == 0: # 위로
        if r == 0:
            return False
        for i in range(w):
            check_list.append((r-1,c+i))
    elif direct == 1: # 오른쪽으로
        if c + w == N:
            return False
        for i in range(h):
            check_list.append((r+i,c+w))
    elif direct == 2: # 아래로
        if r + h == N:
            return False
        for i in range(w):
            check_list.append((r+h,c+i))
    else: # 왼쪽으로
        if c == 0:
            return False
        for i in range(h):
            check_list.append((r+i,c-1))

    neighbors = set()
    for x, y in check_list:
        if map_grid[x][y] == 2:
            return False
        # 범위 안인데 다른 기사가 있다면
        if knight_grid[x][y]:
            neighbors.add(knight_grid[x][y])

    # 인접한 기사들을 모았음
    for neighbor in neighbors:
        if not can_move(neighbor, direct):
            return False

    # 인접한 모든 기사가 갈 수 있으면 나도 갈 수 있음
    return True

def find_loc(idx):
    for x in range(N):
        for y in range(N):
            if knight_grid[x][y] == idx:
                return (x, y)
    return OUT_OF_GRID

def update_hp(idx):
    for x in range(N):
        for y in range(N):
            cur = knight_grid[x][y]
            if cur is not idx and cur in involved:
                if map_grid[x][y] == 1:
                    hp[cur] -= 1
                    damage[cur] += 1
    return

def update_knight_grid():
    for x in range(N):
        for y in range(N):
            if hp[knight_grid[x][y]] <= 0:
                knight_grid[x][y] = 0
    return

def print_ans():
    ans = 0
    for i in range(1,M+1):
        if hp[i] > 0:
            ans += damage[i]
    print(ans)
    return

##############################################

# print_grid(knight_grid)
# print_grid(map_grid)
# print(hp)
# print(damage)
# print(pos)
# print(shield)

for idx, direct in q_list:
    # print("-------------------------")
    # print("query : ",idx, direct)

    moved = try_move(idx,direct)
    # print("moved?:",moved)
    if moved:
        # print("involved:",involved)
        # print_grid(knight_grid)
        update_hp(idx)
        # print("after update hp")
        # print("hp",hp)
        # print("damage",damage)
        update_knight_grid()
        # print("update knight grid")
        # print_grid(knight_grid)

print_ans()