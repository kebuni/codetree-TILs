N, B = map(int,input().split())

gifts = [int(input()) for _ in range(N)]

gifts.sort()
ans = 0

for i in range(N):
    temp_gifts = gifts[:]
    temp_gifts[i] = temp_gifts[i]//2
    num = 0
    temp_B = B
    for k in range(N):
        if temp_B >= temp_gifts[k]:
            temp_B -= temp_gifts[k]
            num += 1
        else:
            break
    
    ans = max(ans,num)

print(ans)