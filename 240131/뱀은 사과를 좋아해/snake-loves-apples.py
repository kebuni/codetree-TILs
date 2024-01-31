from collections import deque
import sys

grid = []
apple = []
snake = deque([])
dxs = [-1,0,1,0]
dys = [0,1,0,-1]
time_elapsed = 0
is_ended = False
head = [0,0]
directs = {'U':0, 'R':1, 'D':2, 'L':3}

#########################

def print_grid(A):
    for i in range(N):
        for j in range(N):
            print(A[i][j],end=' ')
        print()

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def move(direct):
    global head, grid, apple, snake, is_ended
    nx = head[0] + dxs[directs[direct]]
    ny = head[1] + dys[directs[direct]]

    # 만약 범위 밖이거나 몸과 겹치면 리턴
    if not in_range(nx,ny) or (grid[nx][ny] and (nx,ny) != snake[0]):
        is_ended = True
        return

    head[0], head[1] = nx, ny
    grid[nx][ny] = 1
    snake.append((nx,ny))

    # 사과가 있다면 꼬리는 남김
    if apple[nx][ny]:
        apple[nx][ny] = 0 #사과를 없애주고
    else: #사과가 없다면 꼬리 없애야 됨
        tx, ty = snake.popleft()
        grid[tx][ty] = 0

    #print("nx,ny",nx,ny)
    #print("head",head)
    #print(snake)

#########################

N, M, K = map(int,input().split())

for _ in range(N):
    grid.append([0 for i in range(N)])
    apple.append([0 for i in range(N)])

for _ in range(M):
    r,c = map(int,input().split())
    apple[r-1][c-1] = 1

grid[0][0] = 1
snake.append((0,0))

#print_grid(grid)

for _ in range(K):
    direct, dist = input().split()
    dist = int(dist)

    for i in range(dist):
        move(direct)
        time_elapsed += 1
        #print(time_elapsed)
        #print_grid(grid)

        if is_ended:
            #print("end!")
            print(time_elapsed)
            sys.exit(0)

print(time_elapsed)