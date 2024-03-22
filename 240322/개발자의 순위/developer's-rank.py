K, N = map(int,input().split())

below_list = [set() for i in range(N+1)]

for i in range(K):
    line = list(map(int,input().split()))
    high_list = []
    for low in line:
        for high in high_list:
            below_list[high].add(low)
        high_list.append(low)

ans = 0
for high in range(1,N+1):
    for low in range(1,N+1):
        if high == low:
            continue
        
        if high in below_list[low]:
            continue
        else:
            ans += 1

print(ans)