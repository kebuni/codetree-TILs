line = [0 for i in range(101)]

N, K = map(int,input().split())
ans = -1

for i in range(N):
    a, b = map(int,input().split())
    line[b] += a

for i in range(100-(2*K+1)+1):
    sum = 0
    for j in range(2*K+1+1):
        sum += line[i+j]
    #print(sum)
    ans = max(ans, sum)

print(ans)