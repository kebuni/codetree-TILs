import sys

grid = []
ans = -1
move_cnt = 0
direct = 0
visited = []

dxs = [0,1,0,-1]
dys = [1,0,-1,0]

#############################

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def print_grid():
    for i in range(N):
        for j in range(N):
            print(grid[i][j],end=' ')
        print()

def is_there_wall(x,y,direct):
    nx = x + dxs[direct]
    ny = y + dys[direct]
    #assert(in_range(nx,ny))
    if not in_range(nx,ny):
        return False
    return grid[nx][ny] == '#'

def is_original(x,y,direct):
    return visited[x][y][direct]

def print_visited():
    for i in range(N):
        for j in range(N):
            print('[',end=' ')
            for k in range(4):
                if visited[i][j][k]:
                    print("1",end=' ')
                else:
                    print("0",end=' ')
            print(']',end=' ')
        print()
            

#############################

N = int(input())
start_x, start_y = map(int,input().split())
cur_x = start_x - 1
cur_y = start_y - 1

for _ in range(N):
    grid.append(input())
    visited.append([[False for i in range(4)]for j in range(N)])

#print(visited)

while in_range(cur_x,cur_y):
    #print("cnt: ",move_cnt,'/',cur_x,cur_y,direct)

    #print_visited()
    #print(visited)
    
    # 초기 상태로 돌아왔는가? 즉 탈출할 수 없는가?
    if is_original(cur_x,cur_y,direct):
        #print("[-1]")
        #print(cur_x,cur_y,direct)
        print(-1)
        #print_visited()
        sys.exit(0)

    #print(cur_x,cur_y,direct)
    visited[cur_x][cur_y][direct] = True # visited 업데이트
    #print("here")

    if is_there_wall(cur_x,cur_y,direct): # 앞에 벽이 있는 경우
        #print("here3")
        direct = (direct+3)%4
    else: # 앞에 벽 없네,
        nx = cur_x + dxs[direct]
        ny = cur_y + dys[direct]
        #print("here4")

        if not in_range(nx,ny):
            cur_x = nx
            cur_y = ny
            move_cnt += 1
        else:

            if is_there_wall(nx,ny,(direct+1)%4):
                #print("here5")
                cur_x = nx
                cur_y = ny
                move_cnt += 1
            else:
                #print("here6")
                direct = (direct+1) % 4
                cur_x = nx + dxs[direct]
                cur_y = ny + dys[direct]
                move_cnt += 2

print(move_cnt)