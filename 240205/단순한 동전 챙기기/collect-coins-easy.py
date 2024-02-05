grid = []
dxs = [-1,0,1,0]
dys = [0,1,0,-1]
dp = [[-1 for i in range(11)] for j in range(11)]
locations = []
ans = -1
min_temp = 987654321
bag = []
M = 0

######################
def in_range(x,y):
    return 0<=x<N and 0<=y<N

def print_grid():
    for i in range(N):
        for j in range(N):
            print(grid[i][j],end=' ')
        print()

def print_dp():
    for i in range(11):
        for j in range(11):
            print(dp[i][j],end=' ')
        print()

def cal_dist():
    global dp
    size = len(locations)
    for i in range(size):
        num1, x1, y1 = locations[i]
        for j in range(i+1,size):
            num2, x2, y2 = locations[j]
            dp[num1][num2] = abs(x1-x2) + abs(y1-y2)
    return

def choose(n,cnt):
    global bag, min_temp, ans
    if n == M+1:
        if cnt == 3:
            temp = cal_min_dist()
            if min_temp > temp:
                min_temp = temp
                ans = min_temp
        return

    choose(n+1,cnt)
    bag.append(locations[n][0])
    choose(n+1,cnt+1)
    bag.pop()

    return

def cal_min_dist():
    coin1 = bag[0]
    coin2 = bag[1]
    coin3 = bag[2]
    #print(coin1,coin2,coin3)
    return dp[0][coin1] + dp[coin1][coin2] + dp[coin2][coin3] + dp[coin3][10]

######################

N = int(input())
for row in range(N):
    line = input()
    grid.append(line)
    for idx, elem in enumerate(line):
        if elem != '.':
            if elem == 'S':
                locations.append((0,row,idx))
            elif elem == 'E':
                locations.append((10, row, idx))
            else:
                locations.append((int(elem), row, idx))
                M += 1

#print_grid()
locations.sort()
#print(locations)
cal_dist()
#print_dp()

choose(1,0)
print(ans)