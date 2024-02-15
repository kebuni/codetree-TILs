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

# print(customers)
# print(waiting_list)
# print(ans)
# print('----------------')

cus_num = 0
while cus_num < N or waiting_list:
    
    if not waiting_list: # 웨이팅 리스트에 누가 없으면
        start, idx, duration = customers[cus_num]
        cus_num += 1
        end_time = start + duration
        while True:
            if cus_num < N and customers[cus_num][0] < end_time:
                start, idx, duration = customers[cus_num]
                cus_num += 1
                heapq.heappush(waiting_list,(idx,start,duration))
            else:
                break
    else: # 웨이팅 리스트에 누가 있다면
        idx, start, duration = heapq.heappop(waiting_list)
        ans = max(ans,end_time-start)
        end_time = end_time + duration

    # print(customers)
    # print(waiting_list)
    # print(ans)
    # print('----------------')

print(ans)