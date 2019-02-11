import datetime

time = datetime.time(5, 25, 1)

print(time)
print(time.minute)
print(time.hour)
print(datetime.time.max)

date = datetime.date.today()
print(date)

date = date.replace(year=1993)
print(date)
