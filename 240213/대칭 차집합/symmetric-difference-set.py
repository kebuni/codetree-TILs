sizeA, sizeB = map(int,input().split())

A = set(map(int,input().split()))
B = set(map(int,input().split()))

A_B = set()
B_A = set()

for a in A:
    if a not in B:
        A_B.add(a)

for b in B:
    if b not in A:
        B_A.add(b)

print(len(A_B)+len(B_A))