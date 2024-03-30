N,B = map(int,input().split())
digit = []

while True:
    if N < B:
        digit.append(N)
        break
    
    digit.append(N%B)
    N = N//B 

for elem in digit[::-1]:
    print(elem,end='')