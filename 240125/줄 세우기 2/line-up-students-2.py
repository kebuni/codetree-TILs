N = int(input())

arr = []

for i in range(N):
    h, w = map(int,input().split())
    arr.append((h,w,i+1))

arr.sort(key=lambda x: (x[0],-x[1]))

for a,b,c in arr:
    print(a,b,c)