n = int(input())

arr = []
for _ in range(n):
    name, h, w = input().split()
    arr.append((name,int(h),int(w)))

arr.sort(key=lambda x:(x[1],-x[2]))

for a,b,c in arr:
    print(a,b,c)