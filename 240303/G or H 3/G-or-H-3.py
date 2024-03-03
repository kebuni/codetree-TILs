line = [0 for i in range(10001)]

N, K = map(int,input().split())

for i in range(N):
    a, b = input().split()
    a = int(a)
    if b == 'G':
        line[a] = 1
    else:
        line[a] = 2

ans = -1

for i in range(1,10001-(K+1)+1):
    sum = 0
    for j in range(K+1):
        sum += line[i+j]
    ans = max(ans,sum)

print(ans)