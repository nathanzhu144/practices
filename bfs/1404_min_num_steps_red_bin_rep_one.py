# Nathan Zhu April 9th, 2020.  Stockton CA, 9:21 PM PST.  Just finished dinner.
# Leetcode 1404 | medium | not too bad?
# Category: Misc tricks
# This is similar to hailstone

# Dumb, but working soln.
# Wrote this myself.
def numSteps(self, s):
    """
    :type s: str
    :rtype: int
    """
    
    def add_one(arr):
        string = list(arr)
        carry = 1
        i = len(string) - 1
        
        while i >= 0 and carry:
            tot = int(string[i]) + carry
            carry = tot // 2
            string[i] = str(tot % 2)
            i -= 1
        
        if carry == 1: return "1" + "".join(string)
        else: return "".join(string)
    # Edge cases:
    # Empty string, this function fails.
    # Twos compliment.  
    def helper(string):
        if string == "1": return 0
        elif string == "0": return 1
        elif string[-1] == "0":
            return 1 + helper(string[:-1])
        else:
            return 1 + helper(add_one(string))
        
    return helper(s)
    

# Smart but harder soln
#         1001101
#         1001110

#         100111
#         101000

#         10100

#         1010

#         101
#         110

#         11
#         10

#         1
#         After a 1, two operations are performed.  
#         After a 0, one operation is performed.
#         My initial soln fully did out the addition of the 1 if it was odd, however, 
#         this solution does the carry as we go along back to front. 
def numStepsBetter(s):
    """
    :type s: str
    :rtype: int
    """

    N = len(s)
    ret, carry = 0, 0
    for i in range(N - 1, 0, -1):
        if carry + int(s[i]) == 1: 
            ret += 2
            carry = 1
        else: ret += 1
    
    # The reasoning behind ret + carry is kinda untuitive.  The ideae is that since we don't "look" at index 0 in our for loop, if we have a carry
    # we can miss one iteration in our for loop.
    # Ex. 11
    # 11
    # 100
    # 10 <- extra iteration?
    # 1
    #
    # Compare to 10
    # 10
    # 1
    #    
    return ret + carry  

if __name__ == "__main__":
    pass