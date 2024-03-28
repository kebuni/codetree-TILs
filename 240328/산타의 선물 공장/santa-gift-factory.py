from collections import defaultdict
MAX_M = 10
N, M, Q = -1, -1, -1
weight = {}
prev = defaultdict(lambda :0)
next = defaultdict(lambda :0)
head = [0 for i in range(MAX_M)]
tail = [0 for i in range(MAX_M)]
broken = [False for i in range(MAX_M)]
belt_num = defaultdict(lambda :-1)
##################

def build_factory(command):
    global N, M

    N, M = command[1], command[2]
    ids, ws = command[3:3+N], command[3+N:3+2*N]

    for i in range(N):
        weight[ids[i]] = ws[i]

    size = N // M
    for i in range(M):
        head[i] = ids[i*size]
        tail[i] = ids[(i+1)*size-1]
        for j in range(i*size,(i+1)*size):
            belt_num[ids[j]] = i
            if j < (i+1) * size - 1:
                next[ids[j]] = ids[j+1]
                prev[ids[j+1]] = ids[j]

    return

def drop_off(command):
    w_max = command[1]
    w_sum = 0
    for i in range(M):
        if broken[i]:
            continue
        if head[i] != 0:
            _id = head[i]
            w = weight[_id]

            if w <= w_max:
                w_sum += w
                remove_id(_id, True)
            elif next[_id] != 0:
                remove_id(_id, False)
                push_id(tail[i],_id)

    print(w_sum)
    return

def remove(command):
    r_id = command[1]

    if belt_num[r_id] == -1:
        print(-1)
        return

    remove_id(r_id,True)
    print(r_id)

    return

def find(command):
    f_id = command[1]

    if belt_num[f_id] == -1:
        print(-1)
        return

    b_num = belt_num[f_id]
    if head[b_num] != f_id:
        original_tail = tail[b_num]
        original_head = head[b_num]

        new_tail = prev[f_id]
        tail[b_num] = new_tail
        next[new_tail] = 0

        next[original_tail] = original_head
        prev[original_head] = original_tail

        head[b_num] = f_id

    print(b_num + 1)

    return

def broken_belt(command):
    b_num = command[1] - 1

    if broken[b_num]:
        print(-1)
        return

    broken[b_num] = True

    if head[b_num] == 0:
        print(b_num+1)
        return

    next_num = b_num
    while True:
        next_num = (next_num + 1) % M
        if not broken[next_num]:
            if tail[next_num] == 0:
                head[next_num] = head[b_num]
                tail[next_num] = tail[b_num]
            else:
                push_id(tail[next_num], head[b_num])
                tail[next_num] = tail[b_num]

            _id = head[b_num]
            while _id != 0:
                belt_num[_id] = next_num
                _id = next[_id]

            head[b_num] = tail[b_num] = 0
            break

    print(b_num + 1)
    return

def remove_id(_id, remove_belt):
    b_num = belt_num[_id]
    if remove_belt:
        belt_num[_id] = -1

    if head[b_num] == tail[b_num]:
        head[b_num] = tail[b_num] = 0

    elif _id == head[b_num]:
        _next = next[_id]
        head[b_num] = _next
        prev[_next] = 0
    elif _id == tail[b_num]:
        _prev = prev[_id]
        tail[b_num] = _prev
        next[_prev] = 0
    else:
        _prev = prev[_id]
        _next = next[_id]
        prev[_next] = _prev
        next[_prev] = _next

    next[_id] = prev[_id] = 0

    return

def push_id(target_id, _id):
    next[target_id] = _id
    prev[_id] = target_id

    b_num = belt_num[target_id]
    if tail[b_num] == target_id:
        tail[b_num] = _id
    return

##################

Q = int(input())
for _ in range(Q):
    command = list(map(int,input().split()))

    if command[0] == 100:
        build_factory(command)
    elif command[0] == 200:
        drop_off(command)
    elif command[0] == 300:
        remove(command)
    elif command[0] == 400:
        find(command)
    else:
        broken_belt(command)