N = int(input())
arr = list(map(int,input().split()))

ans = 0

for i in range(N):
    for j in range(i,N):

        s = set()
        sum = 0

        for k in range(i,j+1):
            s.add(arr[k])
            sum += arr[k]

        if sum / (j-i+1) in s:
            #print("+1")
            ans+=1

print(ans)