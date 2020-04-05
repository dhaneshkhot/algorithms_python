"""
Sample Input:
08 05 2015
Sample Output:
WEDNESDAY
"""

import calendar
import datetime

input_date = input()
week_day = datetime.datetime.strptime(input_date, '%m %d %Y').weekday()

print(calendar.day_name[week_day].upper())
