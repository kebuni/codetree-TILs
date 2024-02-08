dic = {}

N = int(input())
for i in range(N):
    x, y = map(int,input().split())
    if x not in dic:
        dic[x] = y
    else:
        dic[x] = min(dic[x],y)

sum = 0
for key in dic:
    sum += dic[key]

print(sum)