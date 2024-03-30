m1, d1, m2, d2 = map(int,input().split())
target_date = input()

num_of_days = [0,31,29,31,30,31,30,31,31,30,31,30,31]
date_to_num = {'Mon':0, 'Two':1, 'Wed':2, 'Thu':3, 'Fri':4, 'Sat':5, 'Sun':6}

sum1 = d1
for i in range(m1):
    sum1 += num_of_days[i]

sum2 = d2
for i in range(m2):
    sum2 += num_of_days[i]

ans = (sum2 - sum1) // 7 + 1
if (sum2 - sum1) % 7 < date_to_num[target_date]:
    ans -= 1
print(ans)