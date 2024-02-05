import sys
ans = -(sys.maxsize)
arr = [0,0,0,0,0,0]
dic = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5}
######################

def choose(n):
    global arr, ans
    if n==6:
        #print(arr)
        temp = calculate()
        if temp > ans:
            #print("here!",temp)
            ans = temp
        return
    
    for i in range(1,5):
        arr[n] = i
        choose(n+1)
    
    return

def calculate():
    sum = arr[dic[commands[0]]]
    for i in range(1,N//2+1):
        operator, value = commands[i*2-1], commands[i*2]
        if operator == '+':
            sum += arr[dic[value]]
        elif operator == '-':
            sum -= arr[dic[value]]
        else:
            sum *= arr[dic[value]]
    return sum

######################

commands = input()
N = len(commands)

choose(0)

print(ans)