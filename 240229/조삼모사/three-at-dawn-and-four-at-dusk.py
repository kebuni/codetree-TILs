import sys

N = int(input())
strength = [list(map(int,input().split())) for i in range(N)]

total = 0
for i in range(N):
    for j in range(N):
        total += strength[i][j]

ans = sys.maxsize
selected = []

#############################

def choose(n,m):
    if m == N // 2:
        cal_strength()
        return
    if n == N:
        return

    selected.append(n)
    choose(n+1, m+1)
    selected.pop()
    choose(n+1,m)

    return

def cal_strength():
    global ans
    sum1 = 0
    for row in selected:
        for col in selected:
            sum1 += strength[row][col]

    selected2 = [x for x in range(N) if x not in selected]

    sum2 = 0
    for row in selected2:
        for col in selected2:
            sum2 += strength[row][col]

    temp = abs(sum1-sum2)

    ans = min(ans,temp)

#############################
choose(0,0)
print(ans)