DIGIT_MAX = 5

N = int(input())
arr = []
ans = -1

for i in range(N):
    arr.append(int(input()))

def check_carry(a,b,c):
    for i in range(DIGIT_MAX):
        if a % 10 + b % 10 + c % 10 >= 10:
            return False
        a = a // 10
        b = b // 10
        c = c // 10
    return True

for i in range(N):
    for j in range(i+1,N):
        for k in range(i+1,N):
            if check_carry(arr[i],arr[j],arr[k]):
                ans = max(ans,arr[i]+arr[j]+arr[k])

print(ans)