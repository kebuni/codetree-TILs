N = int(input())
grid = [[0 for i in range(N)] for j in range(N)]
friend_list = [set() for i in range(N*N+1)]
queue = []

dxs = [-1,0,1,0]
dys = [0,1,0,-1]

for i in range(N*N):
    idx, n0, n1, n2, n3 = map(int,input().split())
    queue.append(idx)
    friend_list[idx].add(n0)
    friend_list[idx].add(n1)
    friend_list[idx].add(n2)
    friend_list[idx].add(n3)

################################################

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def go_on_the_ride(idx):
    best = (-1,-1,-1,-1)
    for x in range(N):
        for y in range(N):
            if not grid[x][y]:
                friend_num, blank_num = get_friend_and_blank_num(x,y,idx)
                if best < (friend_num, blank_num, -x, -y):
                    best = (friend_num, blank_num, -x, -y)

    _, _, best_x, best_y = best
    grid[-best_x][-best_y] = idx
    #print("best location for",idx,":",-best_x,-best_y)
    return

def get_friend_and_blank_num(x,y,idx):
    friend_num = 0
    blank_num = 0
    for dx, dy in zip(dxs,dys):
        nx,ny = x + dx, y + dy
        if in_range(nx,ny):
            if grid[nx][ny] in friend_list[idx]:
                friend_num += 1
            if grid[nx][ny] == 0:
                blank_num += 1
    return friend_num, blank_num

def get_score():
    score_sum = 0

    for x in range(N):
        for y in range(N):
            cur = grid[x][y]
            friend_num = 0
            for dx, dy in zip(dxs,dys):
                nx, ny = x + dx, y+dy
                if in_range(nx,ny) and grid[nx][ny] in friend_list[cur]:
                    friend_num += 1
            if friend_num:
                score_sum += 10**(friend_num-1)

    return score_sum

def print_grid():
    for x in range(N):
        for y in range(N):
            print(grid[x][y],end=' ')
        print()
    print()

################################################
for idx in queue:
    go_on_the_ride(idx)

print(get_score())