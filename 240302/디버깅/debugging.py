import copy
import sys

N, M, H = map(int,input().split())
original_selected = []
for _ in range(M):
    original_selected.append(tuple(map(int,input().split())))
selected = []

ans = 100

###############################################

# 현재 selected에 대해 사다리를 내리고 맞으면 True 아니면 False 리턴
def check_bug():

    #print(selected)

    users = [i for i in range(N+1)]
    selected2 = original_selected[:] + selected[:]
    selected2.sort()

    for a, b in selected2:
        temp = users[b]
        users[b] = users[b+1]
        users[b+1] = temp

    for i in range(N):
        if users[i] != i:
            return False

    #print("True!")
    return True

def choose(n,limit):
    global ans

    if n == limit:
        if check_bug():
            print(n)
            sys.exit(0)
        return

    for a in range(1,H+1):
        for b in range(1,N):
            if (a,b) not in original_selected and (a,b-1) not in original_selected and (a,b+1) not in original_selected\
                    and (a,b) not in selected and (a,b-1) not in selected and (a,b+1) not in selected:
                selected.append((a,b))
                choose(n+1,limit)
                selected.pop()

    return

###############################################
selected = []
choose(0,0)
selected = []
choose(0,1)
selected = []
choose(0,2)
selected = []
choose(0,3)

print(-1)