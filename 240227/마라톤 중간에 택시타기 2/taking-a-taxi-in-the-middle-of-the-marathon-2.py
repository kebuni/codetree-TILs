import sys
N = int(input())

check_list = []
dist_list = []
total_dist = 0
ans = sys.maxsize

def taxi_dist(t1,t2):
    return abs(t1[0]-t2[0]) + abs(t1[1]-t2[1])

for i in range(N):
    check_list.append(tuple(map(int,input().split())))

for i in range(1,N):
    taxi_d = taxi_dist(check_list[i],check_list[i-1])
    total_dist += taxi_d
    dist_list.append(taxi_d)

for i in range(1,N-1):
    ans = min(ans,total_dist - dist_list[i-1] - dist_list[i] + taxi_dist(check_list[i-1],check_list[i+1]))

print(ans)