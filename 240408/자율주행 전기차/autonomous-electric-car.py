from collections import deque

INT_MAX = 987654321

N, M, C = map(int,input().split())
grid = [list(map(int,input().split())) for i in range(N)]
start = [[0 for i in range(N)] for j in range(N)]
end = [(-1,-1)]
CX, CY = map(lambda x:int(x)-1,input().split())
for i in range(1,M+1):
    xs, ys, xe, ye = map(int,input().split())
    start[xs-1][ys-1] = i
    end.append((xe-1,ye-1))
fuel = C

dxs = [-1,0,1,0]
dys = [0,1,0,-1]
q = deque()
step = [[-1 for i in range(N)] for j in range(N)]

#####################################################

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def can_go(x,y):
    return in_range(x,y) and step[x][y] == -1 and grid[x][y] == 0

def clear_step():
    for x in range(N):
        for y in range(N):
            step[x][y] = -1
    return

def push(x,y,s):
    step[x][y] = s
    q.append((x,y))
    return

def bfs(x,y):
    clear_step()
    push(x,y,0)
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs,dys):
            nx, ny = x + dx, y + dy
            if can_go(nx,ny):
                push(nx,ny,step[x][y]+1)
    return

def print_grid(A):
    for x in range(N):
        for y in range(N):
            print(A[x][y],end=' ')
        print()
    print()
    return

def get_next_customer():
    # 현재 CX, CY에서 bfs를 합니다.
    bfs(CX,CY)
    # 행, 열을 조사하면서 최소거리인 승객을 찾습니다.
    min_customer = -1
    min_dist = INT_MAX
    min_x, min_y = INT_MAX, INT_MAX
    for x in range(N):
        for y in range(N):
            if start[x][y]:
                if step[x][y] < min_dist:
                    min_dist = step[x][y]
                    min_customer = start[x][y]
                    min_x, min_y = x, y
    # 승객 번호와 좌표 반환

    # print("[get_next_customer]")
    # print("after BFS from",CX,CY)
    # print_grid(step)
    # print("next customer",min_customer,min_x,min_y)

    return min_customer, min_x, min_y

def go_start(customer,cus_x,cus_y):
    global CX, CY, fuel
    # cus_x, cus_y까지의 거리를 구합니다.
    dist = step[cus_x][cus_y]
    # 남은 연료로 이동이 가능한지 봅니다.
    # 불가능하면 return False

    # print("[go_start]")
    # print("dist, fuel",dist,fuel)

    if dist >= fuel:
        # print("not possible")
        return False
    # 가능하면 CX, CY 업데이트
    # 연료 업데이트
    # start 그리드에서 customer를 삭제합니다.
    else:
        CX, CY = cus_x, cus_y
        fuel -= dist
        start[cus_x][cus_y] = 0

    # print("after go start")
    # print("CX, CY", CX, CY)
    # print("fuel",fuel)
    return True

def go_end(customer):
    global CX, CY, fuel
    # 목적지까지 거리를 구합니다.
    ex, ey = end[customer]
    bfs(CX,CY)
    dist = step[ex][ey]
    # 남은 연료로 이동이 가능한지 봅니다.
    # print("[go_end]")
    # print("dist, fuel", dist, fuel)
    # 불가능하면 return False
    if dist > fuel:
        # print("not possible")
        return False
    # 가능하면 CX, CY 업데이트
    # 연료 업데이트, 충전
    else:
        CX, CY = ex, ey
        fuel += dist

    # print("after go start")
    # print("CX, CY", CX, CY)
    # print("fuel", fuel)
    return True

#####################################################
success = 0
for i in range(M):
    customer, cus_x, cus_y = get_next_customer()

    possible = go_start(customer, cus_x, cus_y)
    if not possible:
        break

    possible = go_end(customer)
    if not possible:
        break
    success += 1

# print("done. success:",success)
if success == M:
    print(fuel)
else:
    print(-1)