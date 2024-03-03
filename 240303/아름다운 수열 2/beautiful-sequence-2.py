N, M = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))
B_dic = {}

for i in range(M):
    if B[i] in B_dic:
        B_dic[B[i]] += 1
    else:
        B_dic[B[i]] = 1

ans = 0

for i in range(N-M+1):
    A_dic = {}
    for k in range(M):
        if A[i+k] in A_dic:
            A_dic[A[i+k]] += 1
        else:
            A_dic[A[i+k]] = 1
    if A_dic == B_dic:
        ans += 1

print(ans)