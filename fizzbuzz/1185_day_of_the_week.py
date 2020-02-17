# Nathan Zhu 1:03 am Friday January 3rd, 2020
#                    Sun Feb 12th, 2020 6:00 pm At fishbowl with Zhongfu and Julie
# Leetcode 1185 | easy | not so easy
# Had a very similar problem for my first online assessment at optiver, counting the number of days
# between two dates.  I don't like these problems; I did badly at the onsite when they asked me folloups
# on how to make this approach generalize to billion year timeframes.
# 
# The only things you need to know for this problem:
# 1. How to figure out if a year is a leap year.
# 2. How many days are in each month.
# 3. What day of the week and date today is.
#
#
# Below is a cleaner soln with more python libraries.


def dayOfTheWeek(day, month, year):
    """
    :type day: int
    :type month: int
    :type year: int
    :rtype: str
    """
    def hasLeapDay(year):
        return 1 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 0
    
    # Put TODAY as first day of the week (like today is Friday), and then put next 7 days.
    dayNames = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
    daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    
    def days_since(day, month, year):
        ret = 0
        for y in range(1970, year): 
            ret += (365 + hasLeapDay(y))
            
        for m in range(month - 1):
            ret += daysInMonth[m]
            
        ret += day
        if month > 2 and bool(hasLeapDay(year)): ret += 1
        return ret
    
    # Jan 3rd, 2020, Friday is today.
    days_to_today = days_since(3, 1, 2020)
    days_to_date = days_since(day, month, year)
    
    # Why do we subtract days_to_date from days_to_today?  Well, simple, if the days_to_date is fewer than days to today, it means we have to look in the past
    # Therefore, we have to do a negative modulo.
    # On the other hand, if we look at a date in the future, we would need to calculate a positive modulo.  This generally works out.
    
    return dayNames[(days_to_date - days_to_today) % 7]
            
import calendar
# Sunday Feb 9th, 2020
# 
# ?

# date + (diff % 7) = today.

table = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def dayOfTheWeekUsingCalender(day, month, year):
    def days_since_1971(day, month, year):
        ret = 0
        for y in range(1971, year):
            if calendar.isleap(y): ret += 366
            else: ret += 365
                
        for m in range(1, month):
            # note, feb has 29 days on a leapyear
            ret += calendar.monthrange(year, m)[1]
            
        for d in range(1, day):
            ret += 1
            
        return ret

    return table[(0 - (days_since_1971(9, 2, 2020) - days_since_1971(day, month, year)) % 7)]

if __name__ == "__main__":
    print(dayOfTheWeek(31, 8, 2015))