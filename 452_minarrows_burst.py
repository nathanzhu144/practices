# Nathan Zhu Friday July 19th, 2019 6:25 pm, Amex Building after Fun in the Sun
# Leetcode 452 | medium | medium
# Category: Intervals
# 
# Problem
# There are a number of spherical balloons spread in two-dimensional space. For each
# balloon, provided input is the start and end coordinates of the horizontal 
# diameter. Since it's horizontal, y-coordinates don't matter and hence the 
# x-coordinates of start and end of the diameter suffice. Start is always smaller
# than end. There will be at most 104 balloons.
#
# An arrow can be shot up exactly vertically from different points along the x-axis.
# A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. 
# There is no limit to the number of arrows that can be shot. An arrow once shot
# keeps travelling up infinitely. The problem is to find the minimum number of 
#  arrows that must be shot to burst all balloons.\
#
# Insight:
# So, I'm not 100% sure why this is true, but I *think* this is same as min arrows
# to burst balloons, except we count two touching balloons as overlapping. 
#
# number arrows is same as maximum number of lectures we can schedule in a day,
# so we can use the same algorithm


def min_arrows_burst_balloons(balloons):
    end, cnt = float("-inf"), 0
    for i in sorted(balloons, lambda x: x[1]):
        if i[0] > end:
            end = i[1]
            cnt += 1
    return cnt
