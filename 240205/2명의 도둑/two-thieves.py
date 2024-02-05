ans = -1
grid = []
dp = []
bag = []
temp_max = -1

##############################

def print_dp():
    for i in range(N):
        for j in range(N-M+1):
            print(dp[i][j],end=' ')
        print()

def find_max(x,y):
    global dp, temp_max, bag
    temp_max = -1
    bag = []
    choose(x,y,0,0)
    dp[x][y] = temp_max
    return

def choose(x,y,n,cur_weight):
    global temp_max

    #print(x,y,n)

    if cur_weight > C:
        return
    if n == M:
        price = sum(map(lambda x:x**2,bag))
        temp_max = max(temp_max,price)
        #print(bag)
        return
    
    choose(x,y,n+1,cur_weight)
    bag.append(grid[x][y+n])
    cur_weight += grid[x][y+n]
    choose(x,y,n+1,cur_weight)
    bag.pop()
    cur_weight -= grid[x][y+n]

    return

def choose_region(x,y):
    global ans
    theif1 = dp[x][y]

    for j in range(y+M,N-M+1):
        ans = max(ans,theif1 + dp[x][j])

    for i in range(x+1,N):
        for j in range(N-M+1):
            ans = max(ans,theif1 + dp[i][j])

##############################

N, M, C = map(int,input().split())

for i in range(N):
    grid.append(list(map(int,input().split())))
    dp.append([-1 for _ in range(N-M+1)])

for i in range(N):
    for j in range(N-M+1):
        find_max(i,j)

#print_dp()

for i in range(N):
    for j in range(N-M+1):
        choose_region(i,j)

print(ans)