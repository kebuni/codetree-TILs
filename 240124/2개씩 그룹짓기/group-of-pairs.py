n = int(input())

arr = list(map(int,input().split()))
arr.sort()

A = arr[:n]
B = arr[n:]
B = list(reversed(B))

max = -1
for i in range(n):
    if max < A[i]+B[i]:
        max = A[i]+B[i]

print(max)