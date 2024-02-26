from collections import deque
import sys

q = deque()
ans = sys.maxsize

N = int(input())
for i in range(N):
    q.append(int(input()))

for i in range(N):
    
    temp = q.popleft()
    q.append(temp)

    sum = 0

    for j in range(N):
        sum += q[j]*j

    ans = min(ans,sum)

print(ans)