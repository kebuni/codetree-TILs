from collections import deque

OUT_OF_GRID = (1000,1000)

dxs = [0,1,0,-1]
dys = [1,0,-1,0]
d_to_arrow = ['→','↓','←','↑']

N,M,H,K = map(int,input().split())
hider_grid = [[[] for i in range(N)] for j in range(N)]
next_hider_grid = [[[] for i in range(N)] for j in range(N)]
tree_grid = [[False for i in range(N)] for j in range(N)]
visited = [[False for i in range(N)] for j in range(N)]
step = [[-1 for i in range(N)] for j in range(N)]
seeker_pos = []
seeker_direct = []
seeker_N = 0
sx, sy = N//2 , N//2
q = deque()

for i in range(M):
    x, y, d = map(lambda x:int(x)-1,input().split())
    hider_grid[x][y].append(d)
for i in range(H):
    x, y = map(lambda x: int(x) - 1, input().split())
    tree_grid[x][y] = True

###################################################

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def can_go(x,y,s):
    return in_range(x,y) and not visited[x][y] and (x,y) != (sx,sy) and s

def initialize():
    x, y = sx, sy
    d = 3
    dist_list = []
    for i in range(1,N):
        dist_list.append(i)
        dist_list.append(i)
    dist_list.append(N-1)

    for idx in range(len(dist_list)):
        dist = dist_list[idx]
        for i in range(dist):
            x, y = x + dxs[d], y + dys[d]
            seeker_pos.append((x,y))
            if idx == len(dist_list)-1:
                if i == dist-1:
                    seeker_direct.append((d + 2) % 4)
                else:
                    seeker_direct.append(d)
            else:
                if i == dist -1:
                    seeker_direct.append((d + 1) % 4)
                else:
                    seeker_direct.append(d)
        d = (d + 1) % 4

    d = 1
    for idx in range(len(dist_list)-1,-1,-1):
        dist = dist_list[idx]
        for i in range(dist):
            x, y = x + dxs[d], y + dys[d]
            seeker_pos.append((x, y))
            if idx == 0:
                if i == dist - 1:
                    seeker_direct.append((d + 2) % 4)
                else:
                    seeker_direct.append(d)
            else:
                if i == dist - 1:
                    seeker_direct.append((d - 1 + 4) % 4)
                else:
                    seeker_direct.append(d)
        d = (d - 1 + 4) % 4

    global seeker_N
    seeker_N = len(seeker_pos)
    return

def move_hider():
    clear_next_hider_grid()
    # 우선 술래로 부터 3칸 범위를 bfs로 구합니다
    bfs(sx,sy)
    # 움직이지 않은 도망자는 바로 next로 넣습니다
    # 움직이는 도망자는 처리를 해서 next로 넣습니다
    for x in range(N):
        for y in range(N):
            if step[x][y] == -1: # 움직이지 않는 도망자
                for d in hider_grid[x][y]:
                    next_hider_grid[x][y].append(d)
            else: # 움직이는 도망자
                for d in hider_grid[x][y]:
                    nx, ny, nd = move_hider_one(x,y,d)
                    next_hider_grid[nx][ny].append(nd)
    copy_next_hider_grid()
    return

def move_hider_one(x,y,d):
    nx, ny = x + dxs[d], y + dys[d]
    if in_range(nx,ny):
        if (nx,ny) == (sx,sy):
            return x, y, d
        else:
            return nx, ny, d
    else:
        d = (d+2) % 4
        nx, ny = x + dxs[d], y + dys[d]
        if (nx,ny) == (sx,sy):
            return x, y, d
        else:
            return nx, ny, d


def print_step():
    for x in range(N):
        for y in range(N):
            print(step[x][y],end=' ')
        print()
    print()
    return

def bfs(x,y):
    clear_visited_and_step()
    push(x,y,3)
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs,dys):
            nx, ny = x + dx, y + dy
            if can_go(nx,ny,step[x][y]):
                push(nx,ny,step[x][y]-1)
    return

def push(x,y,s):
    step[x][y] = s
    visited[x][y] = True
    q.append((x,y))
    return

def clear_visited_and_step():
    for x in range(N):
        for y in range(N):
            visited[x][y] = False
            step[x][y] = -1
    return

def clear_next_hider_grid():
    for x in range(N):
        for y in range(N):
            next_hider_grid[x][y].clear()
    return

def copy_next_hider_grid():
    for x in range(N):
        for y in range(N):
            hider_grid[x][y] = next_hider_grid[x][y][:]
    return

def seek(sx,sy,sd,turn_num):
    global score
    x, y = sx, sy
    for i in range(3):
        nx, ny = x + i * dxs[sd], y + i * dys[sd]
        if in_range(nx,ny) and hider_grid[nx][ny] and not tree_grid[nx][ny]:
            score += turn_num * len(hider_grid[nx][ny])
            hider_grid[nx][ny].clear()
    return

def print_hider_grid():
    for x in range(N):
        for y in range(N):
            print("[",end='')
            for elem in hider_grid[x][y]:
                print(d_to_arrow[elem],end='')
            print("]", end=' ')
        print()
    print()
    return

###################################################

score = 0

initialize()
for turn_num in range(K):
    move_hider()
    # print("after move hider")
    # print_hider_grid()

    sx, sy = seeker_pos[(turn_num) % seeker_N ]
    sd = seeker_direct[(turn_num) % seeker_N ]
    # print("after move seeker")
    # print(sx,sy,d_to_arrow[sd])

    seek(sx,sy,sd,turn_num+1)
    # print("after seek")
    # print_hider_grid()
    # print(score)

print(score)