import heapq
import sys

n = int(input())
arr = list(map(int,sys.stdin.readline().split()))
q = []

for i in range(n):
    heapq.heappush(q,arr[i])
    #print(q)
    if i % 2 == 0:
        q_copy = q.copy()
        for j in range(i//2+1):
            ans = heapq.heappop(q_copy)
        print(ans,end=' ')