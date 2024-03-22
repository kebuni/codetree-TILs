X, Y = map(int,input().split())
ans = 0
for i in range(X,Y+1):
    dic = {}
    result = False
    for digit in list(map(int,list(str(i)))):
        if digit not in dic:
            dic[digit] = 1
        else:
            dic[digit] += 1
    if len(dic) == 2:
        for key in dic:
            if dic[key] == 1:
                result = True
    
    if result:
        ans += 1
print(ans)