points = []
selected = []
ans = 987654321
temp_max = -987654321
##########################

def cal_dist(x1,y1,x2,y2):
    return (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)

def cal_all_dist():
    global dp
    for i in range(N):
        x1, y1 = points[i]
        for j in range(i+1,N):
            x2, y2 = points[j]
            dp[i][j] = cal_dist(x1,y1,x2,y2)
    return

def print_dp():
    for i in range(N):
        for j in range(N):
            print(dp[i][j],end=' ')
        print()

def choose(n,cnt):
    global selected,temp_max,ans
    if n == N:
        if cnt == M:
            temp_max = -987654321
            ans = min(ans,find_max())
        return

    choose(n+1,cnt)
    selected.append(n)
    choose(n+1,cnt+1)
    selected.pop()
    return

def find_max():
    global temp_max
    for i in range(M):
        for j in range(i+1,M):
            temp_max = max(temp_max,dp[selected[i]][selected[j]])

    #print("selected : ",selected)
    #print("temp_max : ",temp_max)
    return temp_max

##########################

N, M = map(int,input().split())
dp = [[0 for i in range(N)] for j in range(N)]

for _ in range(N):
    x,y = map(int,input().split())
    points.append((x,y))

cal_all_dist()
#print_dp()

choose(0,0)
print(ans)