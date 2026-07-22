import datetime

current_datetime = datetime.datetime.now()

print(f"Current Date & Time : {current_datetime}")
print(f"Time                : {current_datetime.time()}")
print(f"Day                 : {current_datetime.day}")
print(f"Month               : {current_datetime.month}")
print(f"Year                : {current_datetime.year}")

today = datetime.date.today()
print(f"Today's Date        : {today}")

next_day = today + datetime.timedelta(days=1)
print(f"Next Day            : {next_day}")

date_of_birth = datetime.date(2004, 9, 4)
age = today.year - date_of_birth.year
print(f"Age                 : {age}")