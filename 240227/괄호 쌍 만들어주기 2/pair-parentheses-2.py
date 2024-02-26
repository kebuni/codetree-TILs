string = list(input())

sum = 0
ans = 0

for i in range(1,len(string)):
    if string[i-1] == '(' and string[i] == '(':
        sum += 1
    elif string[i-1] == ')' and string[i] == ')':
        ans += sum

print(ans)