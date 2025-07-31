import time
import calendar

#timestamp
timestamp = time.time()
print(timestamp)

#localtime
local_time = time.localtime()
print(local_time)

#currenttime
current_time = time.localtime(time.time())
print(current_time)

#formatting time
formatting_1 = time.asctime(local_time)
print(formatting_1)

formatting_2 = time.asctime(current_time)
print(formatting_2)

#getting calender for a month
cal = calendar.month(1996,8)
print(cal)