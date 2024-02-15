import heapq
import sys

q =[]
N = int(input())

arr = list(map(int,sys.stdin.readline().split()))

for i in range(N):

    if i == 0:
        heapq.heappush(q,-arr[0])
        print(-1)
    elif i == 1:
        heapq.heappush(q,-arr[1])
        print(-1)
    elif i == 2:
        heapq.heappush(q,-arr[2])
        print(arr[0]*arr[1]*arr[2])
    else:
        heapq.heappush(q,-arr[i])
        heapq.heappop(q)
        print(-q[0]*q[1]*q[2])