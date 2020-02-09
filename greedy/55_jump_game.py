# Nathan Zhu 12:31 pm Jan 20th, 2019 12:31 pm Potbelly, State Street 
# Leetcode 55 | medium | kinda hard without proper insight
# I strugged way too long on this problem, more than a year, for some odd reason.
# I just came back and finished it in 15 min.  I am better now, I think.


def canJumpConcise(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    n, canreach = len(nums), 0
    i = 0
    while i < n and i <= canreach:
        canreach = max(canreach, i + nums[i])
        i += 1
    return i == len(nums)

# Good in the sense you count the number of jumps with this structures.
# Bad in that it is not that concise.
def canJump(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    nextjump = 0
    curridx = 0
    N = len(nums)
    
    while curridx < N:
        oldmax = curridx
        currmax = nextjump
        # count num jumps here.
        while curridx < N and curridx < (currmax + 1):
            nextjump = max(curridx + nums[curridx], nextjump)
            curridx += 1
        if oldmax == curridx: return False
    return True