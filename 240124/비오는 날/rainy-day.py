n = int(input())
forecast = []

min_date = "9999-99-99"
min_index = 999

def earlier(cur_date,min_date):
    curs = cur_date.split('-')
    mins = min_date.split('-')

    if curs[0] < mins[0] : return True
    elif curs[0] > mins[0] : return False
    else:
        if curs[1] < mins[1] : return True
        elif curs[1] > mins[1] : return False
        else:
            if curs[2] < mins[2] : return True
            elif curs[2] > mins[2] : return False

for i in range(n):
    date, day, weather = input().split()
    if weather == 'Rain':
        forecast.append((date,day,weather))

#print(forecast)

for i in range(len(forecast)):
    cur_date, _, _ = forecast[i]
    if earlier(cur_date,min_date):
        min_index = i
        min_date = cur_date
    #print(i,min_date)

print(forecast[min_index][0],forecast[min_index][1],forecast[min_index][2])