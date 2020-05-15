# Nathan Zhu May 7th, 2020. Saw Amber today while walking with Renying, they are abouta have finals.
# Leetcode 303 | easy | kind hard w segment tree
# Category: Segment tree / prefix sum
#
# There's a rlly easy implementation with O(N) preprocess time and O(1) retrieval, but is slow on
# updates.
import collections
class SegmentTree(object):
    def __init__(self, nums):
        self.table = collections.Counter()
        self.arr = nums
        self.build(self.arr)
        
    def build(self, arr):
        def helper(arr, id, l, r):
            if l > r: return           # for empty arr
            if l == r:
                self.table[id] = arr[l]
                return arr[l]
            
            mid = (r - l) // 2 + l
            left = helper(arr, id * 2, l, mid)
            right = helper(arr, id * 2 + 1, mid + 1, r)
            self.table[id] = left + right
            return self.table[id]
        
        helper(arr, 1, 0, len(arr) - 1)
    
    # left, right are inclusive bounds
    def get_sum(self, suml, sumr):
        def helper(suml, sumr, id, l, r):
            if l > r: return 0     # for empty arr
            if suml > r or sumr < l: return 0
            elif suml <= l <= r <= sumr:
                return self.table[id]
            else:
                mid = (r - l) // 2 + l
                left = helper(suml, sumr, id * 2, l, mid)
                right = helper(suml, sumr, id * 2 + 1, mid + 1, r)
                return left + right
        return helper(suml, sumr, 1, 0, len(self.arr) - 1)
    
    # Updates all sums in range(ul, ur) inclusive to assigned
    def update(self, ul, ur, assigned):
        def helper(ul, ur, id, l, r, assigned):
            if l > r: return 0
            if ul > r or ur < l: return self.table[id]
            if l == r:
                self.table[id] = assigned
                return assigned
            else:
                mid = (r - l) // 2 + l
                left = helper(ul, ur, id * 2, l, mid, assigned)
                right = helper(ul, ur, id * 2 + 1, mid + 1, r, assigned)
                self.table[id] = left + right
                return self.table[id]
            
        helper(ul, ur, 1, 0, len(self.arr) - 1, assigned)
        
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.s = SegmentTree(nums)
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.s.get_sum(i, j)
