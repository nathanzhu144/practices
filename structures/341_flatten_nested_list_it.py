# Nathan Zhu Dec 1st, 2019 11:25 pm, Foundry Lofts, Jump Game II
# This one has haunted me for more than a year.
# Leetcode 341 | medium | medium
# Category: Iterator/design
#
# NOTE: Iterators shouldn't copy the internal DS.
#       Also, they should try to save space.
#
# NOTE: A stack is good to furfill both these requirements.
# 
# Given a nested list of integers, implement an iterator to flatten it.
# Each element is either an integer, or a list -- whose elements may also be integers or other lists.

# Example 1:

# Input: [[1,1],2,[1,1]]
# Output: [1,1,2,1,1]
# Explanation: By calling next repeatedly until hasNext returns false, 
#              the order of elements returned by next should be: [1,1,2,1,1].

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """

        self.stack = [[nestedList, 0]]

    def next(self):
        """
        :rtype: int
        """
        self.hasNext()
        if not self.stack: return None

        nested, idx = self.stack[-1]
        self.stack[-1][1] += 1
        return nested[idx].getInteger()

        

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            nested, idx = self.stack[-1]

            if idx == len(nested):
                self.stack.pop()
            else:
                x = nested[idx]
                if x.isInteger(): return True

                self.stack[-1][1] += 1
                self.stack.append([x.getList(), 0])
        return False


