from collections import deque

N, Q = map(int,input().split())
children = [{} for i in range(N+1)]

command = list(map(int,input().split()))
parent = [-1] + command[1:N+1]
authority = [-1] + command[N+1:]

for i in range(1,N+1):
    p = parent[i]
    children[p][i] = True

#######################################

def switch_alarm(c):
    p = parent[c]
    if children[p][c] == True:
        children[p][c] = False
    else:
        children[p][c] = True
    return

def change_authority(c,power):
    authority[c] = power
    return

def switch_parent(c1,c2):
    p1 = parent[c1]
    p2 = parent[c2]

    c1_alarm = children[p1][c1]
    c2_alarm = children[p2][c2]

    children[p1].pop(c1)
    children[p2].pop(c2)

    children[p1][c2] = c2_alarm
    children[p2][c1] = c1_alarm

    parent[c1] = p2
    parent[c2] = p1
    return

def find_alarm(c):
    ans = 0
    stack = deque()
    stack.append((c,0))
    while stack:
        x, dist = stack.pop()
        if x != c and dist <= authority[x]:
            ans += 1
        for next, alarm in children[x].items():
            if alarm:
                stack.append((next, dist+1))
    print(ans)
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