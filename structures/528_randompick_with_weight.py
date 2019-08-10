# Nathan Zhu  EHS 55 John Street 11:50 am Saturday August 3rd, 2019
# Leetcode 528 | medium | medium, if you have seen similar problem
#
# The idea here is to use a presum array, and then randomly choose a number between
# 1 and total sum of array.  Then, do a binary search to find the smallest element bigger
# than the randomly chosen number.
#
# This soln intuitively made a lot of sense for me.
import random

# Here's the idea:
# self.w =  [2, 3, 1]
# self.presum = [2, 5, 6]
# random.randint(1,self.s)
# Then, we can choose a random number between 1 and sum(self.w) == 6.
# 
# seed = random.randint(1, self.totsum)
# 
# We search for the smallest element bigger than the seed, and return that index.
# "Visualization of chances"
# [1, 2] [3, 4, 5] [6]
# The number of chances we can get with this approach would be correct.
# 
class Solution(object):

    def __init__(self, list_in):
        """
        :type w: List[int]
        """
        self.weights = list_in
        self.presum = self.weights[:]

        for i in range(1, len(self.presum)):
            self.presum[i] += self.presum[i - 1]

        self.totalsum = self.presum[-1]

    def pickIndex(self):
        """
        :rtype: int
        """
        seed = random.randint(1, self.totalsum)

        # We do a classic binary search to find the upper bound
        left, right = 0, len(self.presum) - 1
        ret = len(self.presum)  # it is impossible seed > all elements in presum,
                                # but this is good practice

        # Here we do a binary search to find the smallest element greater 
        # or equal to seed, and return that element's index
        while left <= right:
            mid = (left + right) // 2
            if self.presum[mid] == seed: return mid
            if self.presum[mid] > seed:
                ret = mid
                right = mid - 1
            else:
                left = mid + 1

        return ret

if __name__ == "__main__":
    s = Solution([1, 3])
    ret = []
    for i in range(10):
        ret.append(s.pickIndex())

    print(ret)
