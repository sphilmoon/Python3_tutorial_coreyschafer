# naive datetime: no information in daylightsaving or time zone.
import datetime

d = datetime.date(2020, 5, 5) # fixed date.
print(d)

today = datetime.date.today() # today's date.
print(today)

# print(today.weekday()) # Monday 0 Sunday 6
# print(today.isoweekday()) # Monday 1 Sunday 7

timedelta = datetime.timedelta(days=7)
print(today + timedelta) # adding 7 more days to today.

# date2 = date1 + timedelta
# timedelta = date1 + date2

bday = datetime.date(2021, 6, 23)
untill_bday = bday - today
print(untill_bday.days) # how many days left til my next bday.

t = datetime.time(10, 30, 22, 200000) # hr, min, sec, microsec.
print(t)

dt = datetime.datetime(2020, 5, 5, 11, 22, 33, 100000)
print(dt)

dtdelta = datetime.timedelta(hours=10)
print(dt + dtdelta)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow() # for pytz module for timezone.
print(dt_today)
print(dt_now)
print(dt_utcnow)
