# leap year = 366
# normal year = 365
# 4 year once leap year
# To find leap year or not
# 2024 is leap year
# No, the logic for leap years is slightly different. Let me clarify:

# 1. Years that are divisible by 4 are leap years, with one exception.
# 2. Years divisible by 100 are not leap years, with one exception to this exception.
# 3. Years divisible by 400 are leap years.

# So, to determine if a year is a leap year or not:

# - If the year is divisible by 4, it's a leap year.
# - However, if the year is divisible by 100, it's not a leap year, except if:
#   - The year is divisible by 400, then it is a leap year.

# For example:

# - 2000 was a leap year because it's divisible by both 100 and 400.
# - 1900 was not a leap year because it's divisible by 100 but not by 400.
# - 2004 was a leap year because it's divisible by 4 but not by 100.

# This logic helps to keep the calendar synchronized with the Earth's orbit around the sun more accurately.

year = int(input("Enter a Year : "))

if (year % 400 == 0) and (year % 100 == 0):
    print(f'{year} is a Leap Year')
elif (year % 4 == 0) and (year % 100 != 0):
    print(f'{year} is a Leap Year')
else:
    print(f'{year} is not Leap Year')