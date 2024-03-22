X, Y = map(int,input().split())
ans = 0
for i in range(X,Y+1):
    ans = max(ans,sum(list(map(int,list(str(i))))))
print(ans)