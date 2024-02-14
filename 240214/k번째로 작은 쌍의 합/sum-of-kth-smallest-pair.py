import heapq
import sys

MAX_K = 100000
q = []

N, M, K = map(int,input().split())

A = list(map(int,sys.stdin.readline().split()))
A.sort()
B = list(map(int,sys.stdin.readline().split()))
B.sort()

for i in range(N):
    heapq.heappush(q,(A[i]+B[0],i,0))

for i in range(K-1):
    _, idx1, idx2 = heapq.heappop(q)

    idx2 += 1
    if idx2 < M:
        heapq.heappush(q, (A[idx1] + B[idx2], idx1, idx2))

pair_sum, _, _ = heapq.heappop(q)
print(pair_sum)