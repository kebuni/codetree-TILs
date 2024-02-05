arr = []
start = []
ladders = []
temp_ladders = []
result = []
#######################

def get_result():
    global arr
    for _,a in ladders:
        temp = arr[a]
        arr[a] = arr[a+1]
        arr[a+1] = temp

def get_result2():
    global arr
    for _,a in temp_ladders:
        temp = arr[a]
        arr[a] = arr[a+1]
        arr[a+1] = temp

def select(n):
    global ans, arr
    if n == M:
        init_arr()
        get_result2()
        if compare():
            #print("here")
            #print(temp_ladders)
            ans = min(ans,len(temp_ladders))
        return

    #print(n)

    temp_ladders.append(ladders[n])
    select(n+1)
    temp_ladders.pop()
    select(n+1)
    
    return

def compare():
    for i in range(N+1):
        if arr[i] != result[i]:
            return False
    return True

def init_arr():
    global arr
    arr =[]
    for i in range(N+1):
        arr.append(start[i])

#######################

N, M = map(int,input().split())
ans = M

for i in range(N+1):
    start.append(i)

for i in range(M):
    a, b = map(int,input().split())
    ladders.append((b,a))

init_arr()
temp_ladders = []
ladders.sort()
get_result()
#print(arr)

for i in range(N+1):
        result.append(arr[i])

select(0)

print(ans)