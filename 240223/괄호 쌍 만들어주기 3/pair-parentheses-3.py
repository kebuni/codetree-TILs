ans = 0
string = input()

N = len(string)

for i in range(N):
    if string[i] == '(':
        for j in range(i+1,N):
            if string[j] == ')':
                ans += 1

print(ans)