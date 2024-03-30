digit = list(map(int,list(input())))

N = 0
for elem in digit:
    N = N * 2 + elem

N *= 17

arr = []
while True:
    if N < 2:
        arr.append(N)
        break
    
    arr.append(N%2)
    N = N // 2

for elem in arr[::-1]:
    print(elem,end='')