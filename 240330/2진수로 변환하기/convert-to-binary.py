N = int(input())
digit = []

while True:
    if N < 2:
        digit.append(N)
        break
    
    digit.append(N%2)
    N = N // 2

for elem in digit[::-1]:
    print(elem,end='')