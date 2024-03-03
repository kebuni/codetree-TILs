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

def possible(x,s):
    G_num = 0
    H_num = 0
    for i in range(s):
        if line[x+i][1] == 1:
            G_num += 1
        else:
            H_num += 1

    #print(x,s,":",G_num,H_num)

    if G_num == H_num:
        return True
    if G_num == 0:
        return True
    if H_num == 0:
        return True
    return False

for s in range(N,0,-1):
    for x in range(N-s+1):
        if possible(x,s):
            print(line[x+s-1][0] - line[x][0])
            exit(0)