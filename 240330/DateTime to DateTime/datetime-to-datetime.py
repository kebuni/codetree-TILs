import sys

a, b, c = map(int,input().split())

if (11,11,11) > (a,b,c):
    print(-1)
    sys.exit(0)

HOUR_MIN = 60
DAY_MIN = 24*60

sum1 = 11*DAY_MIN + 11*HOUR_MIN + 11
sum2 = a*DAY_MIN + b*HOUR_MIN + c

print(sum2 - sum1)