# Nathan Zhu May 10th, 2020
# Leetcode 732 | hard | this way is pretty hard
# Category: segment tree

import collections



# Update ranges of start, end are inclusive of start, end indices.
# This is a lazy Range-max-query, which supports maximum queries
# 
class Intervals(object):
    def __init__(self):
        self.seg = collections.defaultdict(int)
        self.lazy = collections.defaultdict(int)
        self.rightb = 10 ** 9  # can change this depending on how big appointments get.

    def update(self, start, end):
        # incstart, incend  -  inclusive range we want to increment
        # incamt            -  amount w want to increment all elements in this range by
        # id                -  id of root node, we start with 1 like heap-based index
        # l, r              -  l, r bounds of our array
        def helper(incstart, incend, incamt = 1, id = 1, l = 0, r = self.rightb):
            # Case 1:
            # case of empty interval, do not do anything
            if l > r: return

            # Do update here for lazy.
            if self.lazy[id] != 0:
                self.seg[id] += self.lazy[id]
                # Not a leaf node, propgate lazy to children
                if l != r: 
                    self.lazy[id * 2] += self.lazy[id]
                    self.lazy[id * 2 + 1] += self.lazy[id]
                # reset lazy after propagation
                self.lazy[id] = 0

            # Case 2:
            # no overlap
            if incstart > r or incend < l: return 

            # Case 3:
            # [l, r] is a sub-interval of [incstart, incend]
            elif incstart <= l <= r <= incend:
                self.seg[id] += incamt
                # Lazy update if not leaf node of inc
                if l != r:
                    self.lazy[id * 2] += incamt
                    self.lazy[id * 2 + 1] += incamt

            # Case 4:
            # interval overlap, somewhat, so we need to look down to both children
            else:
                mid = (r - l) // 2 + l
                helper(incstart, incend, incamt, id * 2, l, mid)
                helper(incstart, incend, incamt,  id * 2 + 1, mid + 1, r)
                self.seg[id] = max(self.seg[id * 2], self.seg[id * 2 + 1])
        helper(start, end, 1)

    def find(self, start, end):
        def helper(incstart, incend, id = 1, l = 0, r = self.rightb):
            if l > r: return float('-inf')

            # Propagage lazy if not propagated.
            if self.lazy[id] != 0:
                self.seg[id] += self.lazy[id]
                if l != r:
                    self.lazy[id * 2] += self.lazy[id]
                    self.lazy[id * 2 + 1] += self.lazy[id]
                self.lazy[id] = 0

            # Same as update function mostly
            if incstart > r or incend < l: return float('-inf')
            elif incstart <= l <= r <= incend:
                return self.seg[id]
            else:
                mid = (r - l) // 2 + l
                left = helper(incstart, incend, id * 2, l, mid)
                right = helper(incstart, incend, id * 2 + 1, mid + 1, r)
                return max(left, right)

        return helper(start, end, 1)

class MyCalendarThree(object):
    def __init__(self):
        self.i = Intervals()
        self.ret = 0
        
    def book(self, start, end):
        self.i.update(start, end - 1)   # Interval 
        self.ret = max(self.ret, self.i.find(start, end - 1))
        return self.ret


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
if __name__ == "__main__":
    m = MyCalendarThree()
    print(m.book(1, 2))
    print(m.book(2, 3))
    # m.book(10, 20)
    # m.book(50, 60)
    # m.book(10, 40)
    # m.book(5, 15)
    # m.book(5, 10)
    # m.book(25, 55)
