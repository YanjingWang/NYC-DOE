import datetime
print(datetime.datetime.now())
print(datetime.datetime.now().time())
print(datetime.date.today())

from datetime import date
from datetime import datetime
print(datetime.now())
# print(datetime.now().year())
# print(datetime.now().month())
# print(datetime.now().day())
print(date.today())

now = datetime.now()
print(now)

print(now.strftime("%d %m %Y %H %M %S"))
print(now.strftime("%d/%m/%Y %H:%M:%S"))
print(now.strftime("%d/%B/%Y %H:%M:%S"))
print(date.today().strftime("%d-%m-%Y"))


import datetime
import pytz

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)
dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)

for tz in pytz.all_timezones:
    print(tz)


dt_mtn = datetime.datetime.now()
dt_pacific = dt_mtn.astimezone(pytz.timezone('US/Pacific'))
print(dt_pacific)

dt_mtn = datetime.datetime.now()
mtn_tz = pytz.timezone('US/Mountain')
dt_mtn = mtn_tz.localize(dt_mtn)
print(dt_mtn)

dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn.isoformat())
print(dt_mtn.strftime('%B %d, %Y'))

dt_str = 'July 26, 2022'
dt = datetime.datetime.strptime(dt_str,'%B %d, %Y')
print(dt)

# strftime - datatime to string
# strptime - string to datetime



