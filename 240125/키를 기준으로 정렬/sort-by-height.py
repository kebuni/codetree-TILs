n = int(input())

arr = []

for _ in range(n):
    name, height, weight = input().split()
    height = int(height)
    weight = int(weight)
    arr.append((name,height,weight))

arr.sort(key=lambda x:x[1])

for name, height, weight in arr:
    print(name,height,weight)