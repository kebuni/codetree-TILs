n = int(input())

arr = []

for i in range(n):
    x, y = map(int,input().split())
    arr.append((x,y,i+1))

arr.sort(key=lambda x:(abs(x[0])+abs(x[1]),x[2]))

for _,_,num in arr:
    print(num)