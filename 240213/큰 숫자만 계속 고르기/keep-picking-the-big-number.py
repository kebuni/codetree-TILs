import heapq

q = []

N, M = map(int,input().split())

line = list(map(int,input().split()))

for elem in line:
    heapq.heappush(q,-elem)

for i in range(M):
    x = heapq.heappop(q)
    heapq.heappush(q,x+1)

print(-q[0])