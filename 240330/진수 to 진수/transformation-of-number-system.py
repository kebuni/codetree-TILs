a, b = map(int,input().split())

digit_a = list(map(int,list(input())))
N = 0
for elem in digit_a:
    N = N*a + elem
digit_b = []
while True:
    if N < b:
        digit_b.append(N)
        break
    digit_b.append(N%b)
    N = N // b 
for elem in digit_b[::-1]:
    print(elem,end='')