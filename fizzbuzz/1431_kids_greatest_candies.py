# Nathan Zhu April 2nd, 2020 Biweekly contest
# Leetcode 1431 | easy | easy
# Category: fizzbuzz
# 

def kidsWithCandies(candies, extraCandies):
    N = max(candies)
    
    return [N - candy <= extraCandies for candy in candies]