# Nathan Zhu Thursday, May 28th, 2020, Stockton CA
# Leetcode 1344 | medium | medium
# Category: Misc tricks

def angleClock(h, m):
    """
    :type hour: int
    :type minutes: int
    :rtype: float
    """

    hr_angle = (h % 12 + m / 60.0) * 30  # h % 12 is important man, for cases where hour is 12
    min_angle = (m / 5.0) * 30
    
    ret = abs(hr_angle - min_angle)
    if ret > 180: ret = 360 - ret
    return ret