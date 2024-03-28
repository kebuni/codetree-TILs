from collections import defaultdict
MAX_M = 100000

Q = int(input())
first_command = list(map(int,input().split()))
N, M = first_command[1], first_command[2]
head = [-1 for i in range(N+1)]
tail = [-1 for i in range(N+1)]
gift_num = [0 for i in range(N+1)]
prev, next = [-1] * (MAX_M + 1), [-1] * (MAX_M + 1)

factory = [[] for i in range(N+1)]
for id in range(1,M+1):
    idx = id + 2
    b_num = first_command[idx]
    factory[b_num].append(id)

for b_num in range(N+1):
    if factory[b_num]:
        head[b_num] = factory[b_num][0]
        tail[b_num] = factory[b_num][-1]
        gift_num[b_num] = len(factory[b_num])
        for i in range(len(factory[b_num])-1):
            next[factory[b_num][i]] = factory[b_num][i+1]
            prev[factory[b_num][i+1]] = factory[b_num][i]

############################

def remove_head(b_num):
    if gift_num[b_num] == 0:
        return -1

    if gift_num[b_num] == 1:
        _id = head[b_num]
        head[b_num] = tail[b_num] = -1
        gift_num[b_num] = 0
        return _id

    hid = head[b_num]
    next_head = next[hid]
    next[hid] = prev[next_head] = -1
    gift_num[b_num] -= 1
    head[b_num] = next_head

    return hid

def push_head(b_num, hid):
    if hid == -1:
        return

    if gift_num[b_num] == 0:
        head[b_num] = tail[b_num] = hid
        gift_num[b_num] += 1
    else:
        original_head = head[b_num]
        next[hid] = original_head
        prev[original_head] = hid
        head[b_num] = hid
        gift_num[b_num] += 1

    return

def move_all(m_src, m_dst):

    if gift_num[m_src] == 0:
        print(gift_num[m_dst])
        return

    if gift_num[m_dst] == 0:
        head[m_dst] = head[m_src]
        tail[m_dst] = tail[m_src]
    else:
        original_head = head[m_dst]
        head[m_dst] = head[m_src]
        src_tail = tail[m_src]
        next[src_tail] = original_head
        prev[original_head] = src_tail

    head[m_src] = tail[m_src] = -1
    gift_num[m_dst] += gift_num[m_src]
    gift_num[m_src] = 0

    print(gift_num[m_dst])
    return

def move_half(m_src, m_dst):

    cnt = gift_num[m_src]
    box_ids = []
    for _ in range(cnt//2):
        box_ids.append(remove_head(m_src))

    for i in range(len(box_ids)-1,-1,-1):
        push_head(m_dst,box_ids[i])

    print(gift_num[m_dst])

    return

def exchange(m_src, m_dst):

    src_head = remove_head(m_src)
    dst_head = remove_head(m_dst)
    push_head(m_dst, src_head)
    push_head(m_src, dst_head)

    print(gift_num[m_dst])

    return

def get_gift_info(p_num):
    print(prev[p_num] + 2*next[p_num])
    return

def get_belt_info(b_num):
    print(head[b_num] + 2*tail[b_num] + 3*int(gift_num[b_num]))
    return

############################

for _ in range(Q-1):
    command = list(map(int,input().split()))
    if command[0] == 200:
        move_all(command[1],command[2])
    elif command[0] == 300:
        exchange(command[1],command[2])
    elif command[0] == 400:
        move_half(command[1], command[2])
    elif command[0] == 500:
        get_gift_info(command[1])
    else:
        get_belt_info(command[1])

    # print(next)
    # print(prev)
    # print(head)
    # print(tail)
    # print(gift_num)