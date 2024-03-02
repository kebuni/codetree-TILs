import sys

N, M = map(int,input().split())

grid = []
people = []
hospitals = []
selected = []
ans = sys.maxsize

for x in range(N):
    line = list(map(int,input().split()))
    for y, elem in enumerate(line):
        if elem == 1:
            people.append((x,y))
        elif elem == 2:
            hospitals.append((x,y))

###############################

def choose(n,m):
    global ans
    if m == M:
        ans = min(ans,cal_dist())
        return

    if n == len(hospitals):
        return

    selected.append(hospitals[n])
    choose(n+1,m+1)
    selected.pop()
    choose(n+1,m)
    return

def cal_dist():
    sum = 0
    for x, y in people:
        temp = sys.maxsize
        for hx, hy in selected:
            temp = min(temp,abs(hx-x) + abs(hy-y))
        sum += temp
    return sum

###############################

choose(0,0)
print(ans)