n = int(input())
people = []

for _ in range(n):
    name, address, region = input().split()
    people.append((name, address, region))

people.sort()

a, b, c = people[n-1]
print("name",a)
print("addr",b)
print("city",c)