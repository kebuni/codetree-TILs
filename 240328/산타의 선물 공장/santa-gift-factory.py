import sys

WEIGHT = 0
NEXT = 1
END = -2

Q = int(input())
first_q = list(map(int,sys.stdin.readline().split()))
N = first_q[1]
M = first_q[2]
belt = [{-1:[-1,-2],-2:[-2,-3]} for i in range(M)]
tail = [-1 for i in range(M)]
malfunction = [False for i in range(M)]

for belt_idx in range(M):
    offset1 = belt_idx*(N//M)+3
    offset2 = belt_idx*(N//M)+N+3
    for i in range(N//M):
        id = first_q[offset1+i]
        w = first_q[offset2+i]
        if i == 0:
            belt[belt_idx][-1][NEXT] = id
            belt[belt_idx][id] = [w,first_q[offset1+i+1]]
        elif i == N//M-1:
            tail[belt_idx] = id
            belt[belt_idx][id] = [w,-2]
        else:
            belt[belt_idx][id] = [w,first_q[offset1+i+1]]

query = [list(map(int,input().split())) for i in range(Q-1)]

#################

def process200(wmax):
    weight_sum = 0
    for bi in range(M):
        if malfunction[bi]:
            continue
        cur_head = belt[bi][-1][NEXT]
        if cur_head == -2:
            continue
        cur_weight = belt[bi][cur_head][WEIGHT]
        belt[bi][-1][NEXT] = belt[bi][cur_head][NEXT]
        if cur_weight <= wmax: #하차하기
            weight_sum += cur_weight
            belt[bi].pop(cur_head)
        else: #맨뒤로 옮기기
            cur_tail = tail[bi]
            belt[bi][cur_tail][NEXT] = cur_head
            belt[bi][cur_head][NEXT] = END
            tail[bi] = cur_head
    print(weight_sum)
    return

def process300(rid):
    result = False

    for bi in range(M):
        if malfunction[bi]:
            continue
        if rid in belt[bi]:
            result = True
            prev = belt[bi][-1][NEXT]
            rid_next = belt[bi][rid][NEXT]
            while belt[bi][prev][NEXT] != rid:
                prev = belt[bi][prev][NEXT]
            belt[bi][prev][NEXT] = rid_next
            if tail[bi] == rid:
                tail[bi] = prev
            belt[bi].pop(rid)

    if result:
        print(rid)
    else:
        print(-1)
    return

def process400(fid):
    result_bi = -1
    for bi in range(M):
        if malfunction[bi]:
            continue
        if fid in belt[bi]:
            result_bi = bi + 1
            cur_head = belt[bi][-1][NEXT]
            cur_tail = tail[bi]
            prev = cur_head
            while belt[bi][prev][NEXT] != fid:
                prev = belt[bi][prev][NEXT]
            belt[bi][-1][NEXT] = fid
            belt[bi][cur_tail][NEXT] = cur_head
            tail[bi] = prev
            belt[bi][prev][NEXT] = END

    print(result_bi)
    return

def process500(bnum):
    if malfunction[bnum]:
        print(-1)
        return

    malfunction[bnum] = True
    bi = bnum
    for i in range(1,M):
        bi = (bnum + i) % M
        if not malfunction[bi]:
            break

    cur_tail = tail[bi]
    cur_head = belt[bnum][-1][NEXT]
    while belt[bnum][cur_head][NEXT] != -3:
        w = belt[bnum][cur_head][WEIGHT]
        next = belt[bnum][cur_head][NEXT]
        belt[bi][cur_tail][NEXT] = cur_head
        belt[bi][cur_head] = [w,next]
        belt[bnum].pop(cur_head)
        cur_tail = cur_head
        cur_head = next
    tail[bi] = cur_tail
    tail[bnum] = END
    belt[bi][cur_tail][NEXT] = END
    belt[bnum][-1][NEXT] = END

    print(bnum+1)

    return

#################

for q, num in query:
    if q == 200:
        process200(num)
    elif q == 300:
        process300(num)
    elif q == 400:
        process400(num)
    else:
        process500(num-1)

    # for i in range(M):
    #     print(belt[i])
    # print(tail)