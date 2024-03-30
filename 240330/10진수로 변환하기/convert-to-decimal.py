digit = list(map(int,list(input())))

N = 0
for i in range(len(digit)):
    N = N * 2 + digit[i]

print(N)