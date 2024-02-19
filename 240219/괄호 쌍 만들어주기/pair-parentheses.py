left_num = 0
ans = 0

arr = input()

N = len(arr)

for i in range(1,N):
    if arr[i] == arr[i-1] == '(':
        left_num += 1
    elif arr[i] == arr[i-1] == ')':
        ans += left_num

print(ans)