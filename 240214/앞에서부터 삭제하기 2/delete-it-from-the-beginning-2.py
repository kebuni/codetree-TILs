import heapq
import sys

q = []
ans = -1

N = int(input())

arr = list(map(int,sys.stdin.readline().split()))

heapq.heappush(q,arr[N-1])
heapq.heappush(q,arr[N-2])

min_num = q[0]
avg = q[1]
m = 1

#print(m, min_num, avg, ans)

for i in range(N-3,0,-1):
    heapq.heappush(q, arr[i])
    if min_num > arr[i]:
        avg = (avg*m + min_num) / (m+1)
        min_num = arr[i]
    else:
        avg = (avg*m + arr[i]) / (m+1)
    m += 1
    ans = max(ans,avg)
    #print(m, min_num, avg, ans)

print("%.2f"%ans)