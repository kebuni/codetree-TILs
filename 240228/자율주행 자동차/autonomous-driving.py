N, M = map(int,input().split())
cx, cy, cd = map(int,input().split())

dxs = [-1,0,1,0]
dys = [0,1,0,-1]

grid = [list(map(int,input().split())) for _ in range(N)]
visited = [[False for i in range(M)] for j in range(N)]
visited[cx][cy] = True
keep_status = True

##############################

def move():
    global cx, cy, cd
    # 4방향에 대하여 nx,ny를 확인한다
    # 만약 can_go가 된다면 cx, cy, cd를 업데이트하고 리턴
    for i in range(1,5):
        nd = (cd - i) % 4
        nx = cx + dxs[nd]
        ny = cy + dys[nd]
        if can_go(nx,ny):
            cd,cx,cy = nd,nx,ny
            visited[cx][cy] = True
            return

    # 만약 4방향 다 안되면 후진
    # 후진이 되면 cx, cy, cd를 업데이트하고 리턴
    # 후진이 안되면 keep_status False로 바꾸로 리턴
    nx = cx - dxs[cd]
    ny = cy - dys[cd]
    if in_range(nx,ny) and not grid[nx][ny]:
        cx,cy = nx,ny
        visited[cx][cy] = True
        return
    else:
        global keep_status
        keep_status = False
        return

def in_range(x,y):
    return 0<=x<N and 0<=y<M

def can_go(x,y):
    return in_range(x,y) and not visited[x][y] and not grid[x][y]

##############################

while keep_status:
    move()
    #print(cx,cy,cd)

#rint('------------------------')
ans = 0
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            ans += 1
print(ans)