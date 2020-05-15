# Nathan Zhu May 7th, 2020. Damn I finally got it!!  Called this headhunter today.
# Leetcode 699 | hard | effing damn hard 
# Category: Segment treee with lazy propagation
#
# I'm so proud of this one.  I modified the intervals class, so I could lazily propagate, and also assign a value
# to an interval.
# 
import collections

class Intervals(object):
    def __init__(self):
        self.seg = collections.Counter()
        self.lazy = collections.Counter()
        self.r = 10 ** 9 

    # Takes in a NEW array and builds the interval tree structure from it
    # OVERWRITES old tree structure completely, including size of array
    def build(self, arr):
        def helper(id=1, l=0, r = self.r):
            if l > r: return float('-inf')
            if l == r:
                self.seg[id] = arr[l]
                return arr[l]
            else:
                mid = (r - l) // 2 + l
                left = helper(id * 2, l, mid)
                right = helper(id * 2 + 1, mid + 1, r)
                self.seg[id] = max(left, right)
                return self.seg[id]
        self.seg.clear()
        self.lazy.clear()
        self.r = len(arr) - 1
        helper(1, 0, self.r)

    # Helper functions
    # Push a val k down to children, overwriting their vals
    # Assigns val to each child
    # Assigns val to each child's lazy, so each child can later update their childrens
    #                                   if we propagate further
    # Clears lazy of parent node, as work has been done.
    def push(self, id):
        if self.lazy[id] == 0: return
        self.seg[id * 2] = self.lazy[id]
        self.seg[id * 2 + 1] = self.lazy[id]
        self.lazy[id * 2] = self.lazy[id]
        self.lazy[id * 2 + 1] = self.lazy[id]
        self.lazy[id] = 0

    # Changes range from (addleft, addright) inclusive to amt
    def change(self, addleft, addright, amt):
        def helper(addleft, addright, amt, id=1, l=0, r = self.r):
            if l > r: return
                
            # Case 1 no overlap
            if addleft > r or addright < l: return
            elif addleft <= l <= r <= addright:
                self.seg[id] = amt
                self.lazy[id] = amt
            else:
                self.push(id)
                mid = (r - l) // 2 + l
                helper(addleft, addright, amt, id * 2, l, mid)
                helper(addleft, addright, amt, id * 2 + 1, mid + 1, r)
                self.seg[id] = max(self.seg[id * 2], self.seg[id * 2 + 1])
        helper(addleft, addright, amt)
    
    # Gets max from (incleft, incright).
    def get_max(self, incleft, incright):
        def helper(incleft, incright, id=1, l=0, r=self.r):
            if l > r: return float('-inf')
            if incleft > r or incright < l: return float('-inf')
            self.push(id)

            if incleft <= l <= r <= incright: return self.seg[id]
            else:
                mid = (r - l) // 2 + l
                left = helper(incleft, incright, id * 2, l, mid)
                right = helper(incleft, incright, id * 2 + 1, mid + 1, r)
                return max(left, right)
            
        return helper(incleft, incright)

class Solution(object):
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        s = Intervals()
        ret = []
        max_h = 0
        
        for left, size in positions:
            right = left + size - 1
            
            highest_in_range = s.get_max(left, right)
            s.change(left, right, highest_in_range + size)
            max_h = max(max_h, highest_in_range + size)
            ret.append(max_h)
            
        return ret
            
            



if __name__ == "__main__":
    s = Intervals()
    assert(s.get_max(1, 1000) == 0)
    
    s.build([1, 3, -2, 8, -7])
    assert(s.get_max(0, 0) == 1)
    assert(s.get_max(0, 1) == 3)
    assert(s.get_max(0, 5) == 8)
    assert(s.get_max(1, 2) == 3)
    assert(s.get_max(4, 4) == -7)
    s.change(1,2, -1)
    assert(s.get_max(0, 5) == 8)
    assert(s.get_max(0, 0) == 1)
    assert(s.get_max(1, 2) == -1)
    s.change(1,3, 9)
    assert(s.get_max(0, 5) == 9)
    s.change(2,2, 10)
    assert(s.get_max(0, 5) == 10)
    assert(s.get_max(0, 0) == 1)


# class Solution(object):
#     def fallingSquares(self, positions):
#         """
#         :type positions: List[List[int]]
#         :rtype: List[int]
#         """
        