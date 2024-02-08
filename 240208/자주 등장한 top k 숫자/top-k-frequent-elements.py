import sys

dic = {}
arr = []


N, K = map(int,input().split())
line = list(map(int,sys.stdin.readline().split()))

for elem in line:
    if elem in dic:
        dic[elem] += 1
    else:
        dic[elem] = 1

for key in dic:
    arr.append((dic[key],key))

arr.sort(reverse=True)

for i in range(K):
    print(arr[i][1],end=' ')