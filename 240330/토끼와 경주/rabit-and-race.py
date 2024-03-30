import heapq

Q = int(input())
command = list(map(int,input().split()))
N, M, P = command[1], command[2], command[3]
dist = {}
score = {}
rabit_q = []
for i in range(P):
    pid = command[2*i+4]
    d = command[2*i+4+1]
    dist[pid] = d
    score[pid] = 0
    heapq.heappush(rabit_q,(0,0,0,0,pid))

#############################

def race(K,S):

    best_rabit = -1
    best_record = (-1,-1,-1,-1)

    for i in range(K):
        jump_num, _, x, y, pid2 = heapq.heappop(rabit_q)
        d = dist[pid2]
        candidate = []

        # x, y 로부터 상하좌우 이동한 후 nx, ny를 candidate에 넣기
        # 상하
        nd = d % (2*N-2)
        ux = find_dest_x(x - nd)
        uy = y
        candidate.append((ux + uy, ux, uy))
        dx = find_dest_x(x + nd)
        dy = y
        candidate.append((dx+dy, dx, dy))

        # 좌우
        md = d % (2*M-2)
        rx = x
        ry = find_dest_y(y + md)
        candidate.append((rx+ry,rx,ry))
        lx = x
        ly = find_dest_y(y-md)
        candidate.append((lx+ly,lx,ly))

        # 가장 우선순위 높은 곳 골라서 이동
        _, bx, by = max(candidate)
        heapq.heappush(rabit_q,(jump_num+1,bx+by,bx,by,pid2))

        if (bx+by,bx,by,pid2) > best_record:
            best_rabit = pid2
            best_record = (bx+by,bx,by,pid2)
        #print("pid2:",pid2)

        # 나머지 토끼들에게 점수 추가
        for sid in score:
            if sid != pid2:
                #print("add_score to",sid)
                score[sid] += (bx+by+2)

        # print("race",i)
        # print(rabit_q)
        # print(score)
        # print(dist)

    score[best_rabit] += S

    # print("after race")
    # print(rabit_q)
    # print(score)
    # print(dist)

    return

def find_dest_x(x):
    while x < 0 or x >= N:
        if x < 0:
            x = -x
        elif x >= N:
            x = N - 1 - ( x - (N-1) )
    return x

def find_dest_y(y):
    while y < 0 or y >= M:
        if y < 0:
            y = -y
        elif y >= M:
            y = M - 1 - ( y - (M-1) )
    return y

def change_dist(pid,L):
    dist[pid] *= L
    # print("after change dist")
    # print(rabit_q)
    # print(dist)
    return

def print_best_rabit():
    best_score = 0
    for pid, s in score.items():
        best_score = max(best_score,s)
    print(best_score)
    return

#############################

for _ in range(Q-1):
    command = list(map(int,input().split()))
    if command[0] == 200:
        race(command[1],command[2])
    elif command[0] == 300:
        change_dist(command[1],command[2])
    else:
        print_best_rabit()