from collections import deque

MAX_N = 100001
MAX_D = 22
authority, parent, val = [0] * MAX_N, [0] * MAX_N, [0] * MAX_N
alarm = [False for i in range(MAX_N)]
nx = [[0 for i in range(MAX_D)] for j in range(MAX_N)]
# nx[n][d] = n번째 채팅방이 d depth에 알림을 줄 수 있음

N, Q = map(int,input().split())
command = list(map(int,input().split()))
for i in range(1,N+1):
    parent[i] = command[i]
for i in range(1,N+1):
    authority[i] = command[i + N]
    if authority[i] > 20:
        authority[i] = 20

for i in range(1,N+1):
    cur = i
    x = authority[i]
    nx[cur][x] += 1
    while parent[cur] and x:
        cur = parent[cur]
        x -= 1
        if x:
            nx[cur][x] += 1
        val[cur] += 1

#######################################

def switch_alarm(c):
    cur = parent[c]
    num = 1
    while cur:
        for i in range(num,22):
            val[cur] += nx[c][i] if alarm[c] else -nx[c][i]
            if i > num:
                nx[cur][i-num] += nx[c][i] if alarm[c] else -nx[c][i]
        if alarm[cur]:
            break
        cur = parent[cur]
        num += 1
    alarm[c] = not alarm[c]
    return

def change_authority(c,power):
    bef_power = authority[c]
    power = min(power, 20)  # 권한의 크기를 20으로 제한합니다.
    authority[c] = power

    nx[c][bef_power] -= 1
    if not alarm[c]:
        cur = parent[c]
        num = 1
        # 상위 채팅으로 이동하며 nx와 val 값을 갱신합니다.
        while cur:
            if bef_power >= num:
                val[cur] -= 1
            if bef_power > num:
                nx[cur][bef_power - num] -= 1
            if alarm[cur]:
                break
            cur = parent[cur]
            num += 1

    nx[c][power] += 1
    if not alarm[c]:
        cur = parent[c]
        num = 1
        # 상위 채팅으로 이동하며 nx와 val 값을 갱신합니다.
        while cur:
            if power >= num:
                val[cur] += 1
            if power > num:
                nx[cur][power - num] += 1
            if alarm[cur]:
                break
            cur = parent[cur]
            num += 1
    return

def switch_parent(c1,c2):
    original_alarm1 = alarm[c1]
    original_alarm2 = alarm[c2]

    if not alarm[c1]:
        switch_alarm(c1)
    if not alarm[c2]:
        switch_alarm(c2)

    parent[c1], parent[c2] = parent[c2], parent[c1]

    if not original_alarm1:
        switch_alarm(c1)
    if not original_alarm2:
        switch_alarm(c2)
    return

def find_alarm(c):
    print(val[c])
    return

#######################################
for _ in range(Q-1):
    command = list(map(int,input().split()))
    if command[0] == 200:
        switch_alarm(command[1])
    elif command[0] == 300:
        change_authority(command[1],command[2])
    elif command[0] == 400:
        switch_parent(command[1],command[2])
    else:
        find_alarm(command[1])