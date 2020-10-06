# timezone aware pytz:
import datetime
import pytz

dt = datetime.datetime(2020, 5, 5, 11, 30, 30, tzinfo = pytz.UTC) # UTC offset.
print(dt)

dt_utcnow = datetime.datetime.now(tz = pytz.UTC) # adding miliseconds.
print(dt_utcnow)

# for tz in pytz.all_timezones:
#    print(tz)
dt_rok = dt_utcnow.astimezone(pytz.timezone('ROK')) # ROK is +9hrs to UTC tz.
print(dt_rok)

# making naive time to aware timezone:
dt_cuba = datetime.datetime.now()
cuba_tz = pytz.timezone('Cuba')
dt_cuba = cuba_tz.localize(dt_cuba) # localize makes naive tz aware.
print(dt_cuba) # Cuba is -4hrs to UTC tz.

# strftime - Datetime to string

print(dt_cuba.strftime('%B %d, %Y')) # Find the format code from the website.

# strptime - String to datetime.
dt_str = 'May 5, 2020'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)
