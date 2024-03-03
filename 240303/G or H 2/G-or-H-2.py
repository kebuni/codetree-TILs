import sys

line = []

N = int(input())
for _ in range(N):
    x, c = input().split()
    x = int(x)
    if c == 'G':
        line.append((x,1))
    else:
        line.append((x,2))

line.sort()
#print(line)
ans = -1

for i in range(N):
    for j in range(i,N):

        G_num, H_num = 0, 0
        for k in range(i,j+1):
            if line[k][1] == 1:
                G_num += 1
            else:
                H_num += 1
        if G_num == H_num or G_num == 0 or H_num == 0:
            size = line[j][0] - line[i][0]
            ans = max(ans,size)

print(ans)