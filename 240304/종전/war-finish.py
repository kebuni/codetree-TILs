import sys
from collections import deque

N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]
tribe_grid = [[0 for i in range(N)] for j in range(N)]
visited = [[False for i in range(N)] for j in range(N)]

dxs = [-1,0,1,0]
dys = [0,1,0,-1]
q = deque()

ans = sys.maxsize

########################################################

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def can_go(x,y):
    return in_range(x,y) and not visited[x][y] and tribe_grid[x][y] == 0

def cal_diff(p1,p2,p3,p4):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4

    for x in range(x3):
        tribe_grid[x][y3] = 2
    for x in range(x1+1,N):
        tribe_grid[x][y1] = 5
    for y in range(y4):
        tribe_grid[x4][y] = 4
    for y in range(y2+1,N):
        tribe_grid[x2][y] = 3

    clear_visited()
    push(0,0,2)
    push(0,N-1,3)
    push(N-1,0,4)
    push(N-1,N-1,5)
    push(x1-1,y1,1)
    bfs()

    tribes = [0,0,0,0,0,0]
    for x in range(N):
        for y in range(N):
            tribes[tribe_grid[x][y]] += grid[x][y]

    tribe_max = -1
    tribe_min = 987654321
    for i in range(1,6):
        tribe_max = max(tribe_max,tribes[i])
        tribe_min = min(tribe_min,tribes[i])

    # print_tribe_grid()
    # print(tribes)
    # print(tribe_max - tribe_min)
    # print('---------------------------------')

    return tribe_max - tribe_min

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx,ny):
                push(nx,ny,tribe_grid[x][y])
    return

def push(x,y,t):
    tribe_grid[x][y] = t
    visited[x][y] = True
    q.append((x,y))
    return

def clear_tribe_grid():
    for i in range(N):
        for j in range(N):
            tribe_grid[i][j] = 0
    return

def clear_visited():
    for i in range(N):
        for j in range(N):
            visited[i][j] = False
    return

def try_lectangle(x,y):
    global ans
    # x, y로부터 시작해서 직사각형을 그려봅니다
    # valid한 직사각형일 경우, 부족의 수를 계산하여 ans를 업데이트 합니다.

    for r in range(1,20):
        for l in range(1,20):

            # 오른쪽 위로 갈 칸 l, 왼쪽 위로 갈 칸 r이 정해졌습니다.
            if in_range(x-r,y+r) and in_range(x-r-l,y+r-l) and in_range(x-l,y-l):

                clear_tribe_grid()

                for i in range(r):
                    tribe_grid[x-i][y+i] = 1
                    tribe_grid[x-l-i][y-l+i] = 1
                for j in range(l):
                    tribe_grid[x-j][y-j] = 1
                    tribe_grid[x-r-j][y+r-j] = 1
                tribe_grid[x-r-l][y+r-l] = 1

                #print_tribe_grid()

                temp = cal_diff((x,y),(x-r,y+r),(x-r-l,y+r-l),(x-l,y-l))
                ans = min(ans,temp)


    return

def print_tribe_grid():
    for i in range(N):
        for j in range(N):
            print(tribe_grid[i][j],end=' ')
        print()
    print()

########################################################

for x in range(2,N):
    for y in range(1,N-1):
        try_lectangle(x,y)

print(ans)