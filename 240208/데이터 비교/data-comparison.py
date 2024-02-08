import sys

N = int(input())
s1 = set(map(int,sys.stdin.readline().split()))

M = int(input())
arr2 = list(map(int,sys.stdin.readline().split()))

#print(s1,s2)

for elem in arr2:
    if elem in s1:
        print(1,end=' ')
    else:
        print(0,end=' ')