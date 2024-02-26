N = int(input())

arr = list(input())

ans = 0
C_num = 0
O_num = 0

for elem in arr:
    if elem == 'C':
        C_num += 1
    elif elem == 'O':
        O_num += 1
    elif elem == 'W':
        ans += C_num * O_num

print(ans)