#Simple Alarm Clock: Ask the user to set a time, and when that time is reached, display a message.

import datetime
import time

alarm = input("For when do you want to set the alarm? Please provide hour:minute in 24-hour format - e.g. 14:24: ")

alarmhour = int(alarm[0:2])
alarmminute = int(alarm[3:])

currenttime = datetime.datetime.now()

alarmtime = currenttime.replace(hour=alarmhour, minute=alarmminute, second=0, microsecond=0)

if currenttime > alarmtime:
    alarmtime = alarmtime + datetime.timedelta(days=1)

time_difference = alarmtime - currenttime

time.sleep(time_difference.total_seconds())

print("Your alarm is set for now:", alarmtime)
