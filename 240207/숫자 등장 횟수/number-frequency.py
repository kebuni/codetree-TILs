import sys

dic = {}

N, M = map(int,input().split())

arr = list(map(int,sys.stdin.readline().split()))

for elem in arr:
    if elem in dic:
        dic[elem] += 1
    else:
        dic[elem] = 1

question = list(map(int,sys.stdin.readline().split()))

for elem in question:
    if elem in dic:
        print(dic[elem],end=' ')
    else:
        print(0,end=' ')