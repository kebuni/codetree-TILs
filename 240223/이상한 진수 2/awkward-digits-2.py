A = list(input())

N = len(A)

no_zero = True

for i in range(N):
    if A[i] == '0':
        no_zero = False
        A[i] = '1'
        break

if no_zero:
    A[N-1] = '0'

#print(A)
ans = 0
for i in range(N):
    if A[N-i-1] == '1':
        ans += 2**i

print(ans)