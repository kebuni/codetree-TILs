n = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort()
ans = "Yes"

for i in range(n):
    if A[i] != B[i]:
        ans = "No"
        break

print(ans)