m1, d1, m2, d2 = map(int,input().split())

num_of_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

sum1 = d1
for i in range(m1):
    sum1 += num_of_days[i]

sum2 = d2
for i in range(m2):
    sum2 += num_of_days[i]

print(sum2-sum1+1)