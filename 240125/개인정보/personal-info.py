arr = []

for _ in range(5):
    name, height, weight = input().split()
    arr.append((name,int(height),float(weight)))

arr.sort(key=lambda x:x[0])

print("name")
for name, height, weight in arr:
    print(name,height,weight)
print()

arr.sort(key=lambda x:-x[1])

print("height")
for name, height, weight in arr:
    print(name,height,weight)