# Nathan Zhu January 4th, 2019 2:08 pm
# Leetcode 66 | easy | easy
# Category: math/misc tricks

# Only tricky part is if we have a carry bit at the very end, this has to be managed appropriately.
def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    digits[-1] += 1
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] <= 9: break
        
        if i == 0:
            # Note that inserting moves the list itself, so we need an extra case for digits[i]
            digits.insert(0, 1)
            digits[1] %= 10
        else: 
            digits[i - 1] += 1
            digits[i] %= 10
    return digits
                