# Friday July 5th, 2019.  Nathan Zhu YOTEL, New york New york, was up into 6 am with Peifu last night.
# Leetcode 415 | easy | easy
#
# I learned a new trick with the "replacing trick" last time.  Runtime is O(max(len(num1, num2))),
#                                                          but less eelegant way is O(min(num1, num2))
def addStrings(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    num2 = num2[::-1]
    num1 = num1[::-1]
    ret = []
    
    num1_i, num2_i, overflow = 0, 0, 0
    while num1_i < len(num1) or num2_i < len(num2):
        # One insight here is that num1 or num2 could be shorter. This is an elegant way of doing that.
        # We stop the loop only when both indices are out of range, but if an index is out of range,
        # we replace the desired number with a 0.
        num1_num, num2_num = 0, 0
        if num1_i < len(num1): num1_num = int(num1[num1_i])
        if num2_i < len(num2): num2_num = int(num2[num2_i])
            
        ret.append((num1_num + num2_num + overflow) % 10)    # adds current integer
        overflow = (num1_num + num2_num + overflow) // 10    # tracks the carry
        num1_i += 1
        num2_i += 1
    
    # DON'T FORGET THIS LINE. We need to add on the overflow at the very end.
    ret.append(overflow)
    returned = "".join(str(n) for n in ret[::-1])
    # without this line, I was returning stuff with leading 0s.
    return str(int(returned))

if __name__ == "__main__":
    print(addStrings("99", "9"))