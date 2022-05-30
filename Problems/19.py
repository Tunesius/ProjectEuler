# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

current_day = 1
current_month = 1
current_year = 1901
current_day_name = 2
counter = 0


def is_leap_year():
    if current_year % 400 == 0:
        return True
    if current_year % 100 != 0 and current_year % 4 == 0:
        return True
    return False


def should_increase_month():
    if (current_month == 4 or current_month == 6 or current_month == 11 or current_month == 9) and current_day == 30:
        return True
    elif (is_leap_year() and current_month == 2 and current_day == 29) or ((not is_leap_year()) and current_month == 2 and current_day == 28):
        return True
    elif current_day == 31:
        return True
    return False


def increase_date():
    global current_month
    global current_day
    global current_year
    if should_increase_month():
        if current_month == 12:
            current_month = 1
            current_day = 1
            current_year = current_year + 1
        else:
            current_month = current_month + 1
            current_day = 1
    else:
        current_day = current_day + 1


def increase_day():
    global current_day_name
    current_day_name = current_day_name + 1
    if current_day_name == 8:
        current_day_name = 1


while not current_year == 2001:
    increase_date()
    increase_day()
    if current_day == 1 and current_day_name == 7:
        counter = counter + 1

print(counter)
