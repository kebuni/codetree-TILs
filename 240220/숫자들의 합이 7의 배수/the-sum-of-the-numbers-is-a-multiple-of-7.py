N = int(input())
arr = []
dic = {}
Two = [0 for i in range(7)]
ans = 0

for _ in range(N):
    arr.append(int(input()))

arr[0] = arr[0] % 7
for i in range(1,N):
    arr[i] = (arr[i-1] + arr[i]) % 7

#print(arr)

for idx, elem in enumerate(arr):
    if elem == 0:
        ans = 1
    if elem not in dic:
        dic[elem] = idx
    else:
        Two[elem] = idx - dic[elem]

for i in range(7):
    ans = max(ans,Two[i])

print(ans)