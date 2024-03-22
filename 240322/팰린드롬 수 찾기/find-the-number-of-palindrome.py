X, Y = map(int,input().split())
ans = 0
for i in range(X,Y+1):
    A = list(map(int,list(str(i))))
    B = list(reversed(A))
    result = True
    for k in range(len(A)):
        if A[k] != B[k]:
            result = False
    if result:
        ans += 1
print(ans)