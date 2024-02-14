import heapq
q = []

N = int(input())

arr = list(map(int,input().split()))

for elem in arr:
    heapq.heappush(q,-elem)

#print(q)

while len(q) > 1:
    a = -heapq.heappop(q)
    b = -heapq.heappop(q)

    if a != b:
        heapq.heappush(q,-abs(a-b))

    #print(q)

if q:
    print(-q[0])
else:
    print(-1)