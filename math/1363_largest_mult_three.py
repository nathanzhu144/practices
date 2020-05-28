# Nathan Zhu May 21st, 2020, 3rd day at Salesforce just finished!
# Leetcode 1363 | hard | ok-ish
# Category: Math
# Runtime: NlogN, but possible w O(N) with a reverse-bucket sort
#d
# Here's the idea, multiples of 3 have sum of digits be a multiple of 3.
# If sum(digits) % 3 == 0, we can use all digits
# However, if sum(digits) % 3 == 1 we either have one extra one, or two extra twos.  The first option gives a bigger number
# but is not always possible to take.
# Furthermore, if sum(digits) % 3 == 2, we have one extra two or two extra ones.s
#
# 

def largestMultipleOfThree(self, digits):
    """
    :type digits: List[int]
    :rtype: str
    """
    if all([num == 0 for num in digits]): return "0"
    
    digits.sort(reverse=True)
    zeroes, ones, twos = [], [], []
    for num in digits:
        if num % 3 == 0: zeroes.append(num)
        elif num % 3 == 1: ones.append(num)
        else: twos.append(num)
            
    
    tot = sum(digits)
    ret = ones + twos + zeroes
    if tot % 3 == 1:
        if(ones):
            ret = ones[:-1] + twos + zeroes
        else:
            ret = ones + twos[:-2] + zeroes
    elif tot % 3 == 2:
        if twos:
            ret = ones + twos[:-1] + zeroes
        else:
            ret = ones[:-2] + twos + zeroes
            
    ret.sort(reverse=True)
    return "".join(map(str, ret))
            
    