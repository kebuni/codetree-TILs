import heapq

N, M = map(int,input().split())
q = []

for i in range(N):
    x, y = map(int,input().split())
    heapq.heappush(q,(abs(x)+abs(y),x,y))

for i in range(M):
    _, x, y = heapq.heappop(q)
    x += 2
    y += 2
    heapq.heappush(q,(abs(x)+abs(y),x,y))

_, x, y = heapq.heappop(q)
print(x,y)