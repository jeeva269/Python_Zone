# Date Time Functions in Python

import datetime as dt


current_date=dt.date.today()
print("Current Date :",current_date )

'New date create'

new=dt.date(2024,8,31)
print(new)
print("year : ", new.year)
print("Month : ", new.month)
print("Day : ", new.day)

print("----------------------------------")

'New time create'

a=dt.time(10,45,5,555505)
print(a)
print("Hour : ", a.hour)
print("minute : ", a.minute)
print("second : ", a.second)
print("micrsecond : ", a.microsecond)

print("----------------------------------")

'current time check'

current_time=dt.datetime.now()
print("Current Time : ", current_time)

print("----------------------------------")

'timedate naba set pannikalaa'

new=dt.datetime(2024,9,30,12,5,10)
print(new)
print(new.date())
print(new.time())

print("----------------------------------")

'next year count days'

current = dt.datetime.now()
new_year = dt.datetime(2025, 1, 1)
difference = new_year - current
print(difference)

print("----------------------------------")

'show words in date and month'

current= dt.datetime.now()
print(current)
s=current.strftime("%A %B %D %Y")
print(s)