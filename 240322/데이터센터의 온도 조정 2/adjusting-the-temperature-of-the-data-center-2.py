N, C, G, H = map(int,input().split())
temp_list = [tuple(map(int,input().split())) for i in range(N)]

def get_work(i,t):
    ta, tb = temp_list[i]
    if t < ta:
        return C
    elif t > tb:
        return H
    else:
        return G 

ans = 0
for t in range(-1,1001):
    temp = 0
    for i in range(N):
        temp += get_work(i,t)
    ans = max(ans,temp)
print(ans)