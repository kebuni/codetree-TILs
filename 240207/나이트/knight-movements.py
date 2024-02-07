from collections import deque
step = []
visited =[]

dxs = [-2,-2,-1,1,2,2,1,-1]
dys = [-1,1,2,2,1,-1,-2,-2]

q = deque()

#######################

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def can_go(x,y):
    return in_range(x,y) and not visited[x][y]

def push(x,y,s):
    visited[x][y] = 1
    step[x][y] = s
    q.append((x,y))
    return

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs,dys):
            nx = x + dx
            ny = y + dy
            if can_go(nx,ny):
                push(nx,ny,step[x][y]+1)
    return

#######################
N = int(input())
step = [[-1 for i in range(N)]for j in range(N)]
visited = [[0 for i in range(N)]for j in range(N)]

sx, sy, ex, ey  = map(int,input().split())

push(sx-1,sy-1,0)
bfs()

print(step[ex-1][ey-1])