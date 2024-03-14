from collections import deque
OUT_OF_RANGE = 987654321

dxs = [-1,0,1,0]
dys = [0,-1,0,1]
q = deque()

N, M, C = map(int,input().split())
remain_fuel = C
grid = [list(map(int,input().split())) for i in range(N)]
#start_grid = [[0 for i in range(N)] for j in range(N)]
#end_grid = [[0 for i in range(N)] for j in range(N)]
customers = [(OUT_OF_RANGE,OUT_OF_RANGE,OUT_OF_RANGE,OUT_OF_RANGE)]
visited = [[False for i in range(N)] for j in range(N)]
step = [[-1 for i in range(N)] for j in range(N)]
cx, cy = map(lambda x:int(x)-1,input().split())
for i in range(M):
    xs, ys, xe, ye = map(int,input().split())
    #start_grid[xs - 1][ys - 1] = i + 1
    #end_grid[xe - 1][ye - 1] = i + 1
    customers.append((xs-1,ys-1,xe-1,ye-1))
    #print(i+1,xe-1,ye-1)

arrived = [False for i in range(M+1)]

##########################################

def in_range(x,y):
    return 0<=x<N and 0<=y<N

def can_go(x,y):
    return in_range(x,y) and not visited[x][y] and grid[x][y] == 0

def clear_visited_and_step():
    clear_q()
    for x in range(N):
        for y in range(N):
            visited[x][y] = False
            step[x][y] = -1
    return

def push(x,y,s):
    visited[x][y] = True
    step[x][y] = s
    q.append((x,y))
    return

def find_next_customer():
    result = OUT_OF_RANGE
    min_dist = 999999
    result_x, result_y = OUT_OF_RANGE, OUT_OF_RANGE
    clear_visited_and_step()
    push(cx,cy,0)
    while q:
        x, y = q.popleft()
        # 현재 보는 x, y가 손님 위치인지 확인! 손님이면 그 손님 번호 리턴
        #if start_grid[x][y] != 0:
            #return start_grid[x][y], x, y

        for dx, dy in zip(dxs,dys):
            nx, ny = x + dx, y + dy
            if can_go(nx,ny):
                push(nx,ny,step[x][y] + 1)

    for idx in range(1,M+1):
        if not arrived[idx]:
            sx, sy, ex, ey = customers[idx]
            if step[sx][sy] != -1:
                if (step[sx][sy],sx,sy) < (min_dist,result_x,result_y):
                    result = idx
                    result_x, result_y = sx, sy
                    min_dist = step[sx][sy]

    # for x in range(N):
    #     for y in range(N):
    #         if start_grid[x][y] and step[x][y] != -1:
    #             if step[x][y] < min_dist:
    #                 result = start_grid[x][y]
    #                 result_x, result_y = x,y
    #                 min_dist = step[x][y]
    #                 #print("here!", step[x][y], "so result is now", result)

    return result, result_x, result_y

def can_go_to(dest_x,dest_y):

    if (dest_x,dest_y) == (OUT_OF_RANGE,OUT_OF_RANGE):
        return False

    clear_visited_and_step()
    push(cx, cy, 0)
    while q:
        x, y = q.popleft()
        # 현재 보는 x, y가 가려는 위치인지 확인! 맞다면 현재 연료로 갈 수 있는지
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                push(nx, ny, step[x][y] + 1)

    # 갈 수 없으면 false

    return step[dest_x][dest_y] != -1 and step[dest_x][dest_y] <= remain_fuel

def go_to(dx,dy):
    global cx, cy, remain_fuel
    cx, cy = dx, dy
    remain_fuel -= step[dx][dy]
    return step[dx][dy]

def find_destination(idx):
    sx, sy, ex, ey = customers[idx]
    return ex, ey
    # for x in range(N):
    #     for y in range(N):
    #         if end_grid[x][y] == idx:
    #             return x, y
    # return OUT_OF_RANGE, OUT_OF_RANGE

def update_grid(idx):
    customers[idx] = (OUT_OF_RANGE,OUT_OF_RANGE,OUT_OF_RANGE,OUT_OF_RANGE)
    # for x in range(N):
    #     for y in range(N):
    #         if start_grid[x][y] == idx:
    #             start_grid[x][y] = 0
    #         if end_grid[x][y] == idx:
    #             end_grid[x][y] = 0

    arrived[idx] = True
    return

def check_end():
    for i in range(1,M+1):
        if not arrived[i]:
            return False
    return True

def print_status():
    print("car pos: ",cx, cy)
    print("remain fuel: ", remain_fuel)
    print_step()

def print_step():
    for i in range(N):
        for j in range(N):
            print(step[i][j],end=' ')
        print()
    print()

def clear_q():
    while q:
        q.popleft()
    return

# def print_grids():
#     for i in range(N):
#         for j in range(N):
#             print(start_grid[i][j],end=' ')
#         print()
#     print()
#     for i in range(N):
#         for j in range(N):
#             print(end_grid[i][j],end=' ')
#         print()
#     print()

##########################################

ans = -1
success = False

while True:
    customer_idx, sx, sy = find_next_customer()
    if customer_idx == OUT_OF_RANGE:
        # print("here!")
        break

    # print("------------------------------")
    # print("next_customer : ", customer_idx,sx,sy)

    if can_go_to(sx,sy):
        _ = go_to(sx,sy)
    else:
        break

    # print("go to start pos")
    # print_status()

    ex, ey = find_destination(customer_idx)

    if can_go_to(ex,ey):
        used_fuel = go_to(ex,ey)
    else:
        break

    # print("go to end pos")
    # print_status()

    update_grid(customer_idx)
    remain_fuel += used_fuel * 2

    # print("after arrival")
    # print(remain_fuel)
    # print(arrived)
    #print_grids()

    if check_end():
        ans = remain_fuel
        break

print(ans)