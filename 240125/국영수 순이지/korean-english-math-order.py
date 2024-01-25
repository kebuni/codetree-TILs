n = int(input())

arr = []

for _ in range(n):
    name, kor, eng, math = input().split()
    kor = int(kor)
    eng = int(eng)
    math = int(math)
    arr.append((name,kor,eng,math))

arr.sort(key = lambda x: (-x[1],-x[2],-x[3]))

for name, kor, eng, math in arr:
    print(name,kor,eng,math)