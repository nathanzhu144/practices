#  Nathan Zhu, 9:19 pm, New York, Amex Tower
#  Leetcode 169 | easy | lol, I would never have understood the trick on my own.
#
#  This one is a doozy - the trick is genius enough that there's a research paper about it.
#
#  http://www.cs.utexas.edu/~moore/best-ideas/mjrty/
#  It is called moore's voting algorithm.
#
#  Assuming there is an element that exists more than floor(n/2) times in an array, you can find it 
#  in O(n) time, and O(1) space.
#
#  The proof on quora is compelling.
#  https://www.quora.com/What-is-the-proof-of-correctness-of-Moores-voting-algorithm
#
#  Suppose that we have a majority element:
#
#    1. We have two cases.  
#
#  NOTE: Leetcode guarantees a majority element.  If we don't know there is one, you have to double-check.

def majorityElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ret = nums[0]
    
    counter = 1
    for i in range(1, len(nums)):
        if nums[i] == ret: counter += 1
        if nums[i] != ret: counter -= 1
        if counter < 0: 
            ret = nums[i]
            counter = 1
        
    return ret