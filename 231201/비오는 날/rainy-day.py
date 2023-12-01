import datetime
class Weather:
    def __init__(self, date, weekday, weather):
        self.date = date
        self.weekday = weekday
        self.weather = weather

def compare(wet1, wet2):
    date1 = wet1.date
    date2 = wet2.date
    y1, m1, d1 = list(date1.split('-'))
    y2, m2, d2 = list(date2.split('-'))
    if y1 < y2:
        return wet1
    elif y1 > y2:
        return wet2
    else:
        if m1 < m2:
            return wet1
        elif m1 > m2:
            return wet2
        else:
            if d1 < d2:
                return wet1
            elif d1 > d2:
                return wet2
            else:
                return wet2

n = int(input())

Weather_DB = []
for _ in range(n):
    date, weekday, weather = list(input().split())
    Weather_DB.append(Weather(date, weekday, weather))

Rain_DB = []
for weat in Weather_DB:
    if weat.weather == 'Rain':
        Rain_DB.append(weat)

min_d = Rain_DB[0]

for i in range(len(Rain_DB)):
    min_d = compare(min_d, Rain_DB[i])


print(f"{min_d.date} {min_d.weekday} {min_d.weather}")