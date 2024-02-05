import sys

selected = []
ans = -(sys.maxsize)
######################

def choose(n,cnt):
    global selected, ans
    if n == N:
        if cnt == M:
            ans = max(ans,calculate())
            #print(selected)

        return
    
    choose(n+1,cnt)
    selected.append(arr[n])
    choose(n+1,cnt+1)
    selected.pop()

    return

def calculate():
    xor = selected[0]
    for i in range(1,M):
        xor = xor^selected[i]
    return xor

######################
N, M = map(int,input().split())

arr = list(map(int,input().split()))

choose(0,0)

print(ans)