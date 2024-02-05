import sys

selected = []
ans = sys.maxsize
####################################

def choose(n,cnt):
    global selected, ans
    if n == 2*N:
        if cnt == N:
            #print(selected)
            temp_sum = sum(selected)
            ans = min(ans,abs(arr_sum-2*temp_sum))
        return

    choose(n+1,cnt)
    selected.append(arr[n])
    choose(n+1,cnt+1)
    selected.pop()
    return

####################################

N = int(input())
arr = list(map(int,input().split()))

arr_sum = sum(arr)
choose(0,0)

print(ans)