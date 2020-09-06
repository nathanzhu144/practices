
# /* Nathan Zhu  Saturday July 11th, 2020 Stockton, CA, Weekly contest
# *  Leetcode 1507 | easy | easy
# *  Category: misc tricks
# */


import collections
import heapq
import bisect

def reformatDate(date):
    """
    :type date: str
    :rtype: str
    """
    table = dict()
    table["Jan"] = "01"
    table["Feb"] = "02"
    table["Mar"] = "03"
    table["Apr"] = "04"
    table["May"] = "05"
    table["Jun"] = "06"
    table["Jul"] = "07"
    table["Aug"] = "08"
    table["Sep"] = "09"
    table["Oct"] = "10"
    table["Nov"] = "11"
    table["Dec"] = "12"
    
    def get_day(day):
        ret = []
        for ch in day:
            if not ch.isdigit(): 
                if len(ret) == 1: ret = ["0"] + ret
                return "".join(ret)
            ret += ch
    
    unproc_day, unproc_month, year = date.split(" ")
    day = get_day(unproc_day)
    month = table[unproc_month]
    return "-".join([year, month, day])
    