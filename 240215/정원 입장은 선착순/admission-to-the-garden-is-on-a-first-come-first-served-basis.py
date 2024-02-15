import heapq
from collections import deque

customers = []
waiting_list = []
ans = 0
end_time = 0

N = int(input())

for i in range(N):
    start, duration = map(int,input().split())
    customers.append((start,i,duration))

customers.sort()
cus_idx = 0

for i in range(N):
    
    if not waiting_list:
        start, idx, duration = customers[cus_idx]
        cus_idx += 1
        ans = max(ans, end_time - start)
        end_time = start + duration

        while True:
            if cus_idx<N and customers[cus_idx][0] < end_time + duration:
                start, idx, duration = customers[cus_idx]
                cus_idx += 1
                heapq.heappush(waiting_list,(idx, start, duration))
            else:
                break

    else:
        idx, start, duration = heapq.heappop(waiting_list)
        ans = max(ans, end_time - start)
        end_time += duration
        
print(ans)