import sys
dic = {}
ans = 0

N, K = map(int,input().split())
arr = list(map(int,sys.stdin.readline().split()))

for i in range(N-1):
    num1 = arr[i]
    for j in range(i+1,N):
        num2 = arr[j]

        diff = K - num1 - num2
        if diff in dic:
            ans += dic[diff]
    
    if num1 in dic:
        dic[num1] += 1
    else:
        dic[num1] = 1

print(ans)