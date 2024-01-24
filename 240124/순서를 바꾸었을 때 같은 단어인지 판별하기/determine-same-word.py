A = input()
B = input()

A = list(A)
B = list(B)

A.sort()
B.sort()

ans = "NO"

if len(A) == len(B):
    for i in range(len(A)):
        if A[i] != B[i]:
            ans = "NO"
            break
        ans = "YES"



print(ans)