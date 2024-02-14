import heapq

q = []

N = int(input())
for _ in range(N):
    x = int(input())
    if x == 0:
        if q:
            _, ans = heapq.heappop(q)
            print(ans)
        else:
            print(0)
    else:
        heapq.heappush(q,(abs(x),x))