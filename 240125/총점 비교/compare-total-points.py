n = int(input())

arr = []

for _ in range(n):
    name, sub1, sub2, sub3 = input().split()
    arr.append((name,int(sub1),int(sub2),int(sub3)))

arr.sort(key=lambda x : x[1]+x[2]+x[3])

for name, sub1, sub2, sub3 in arr:
    print(name,sub1,sub2,sub3)