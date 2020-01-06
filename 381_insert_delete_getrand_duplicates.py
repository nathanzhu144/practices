# Nathan Zhu 11:07 pm, December 31st, 2019 11:07 pm
# Leetcode 381 | hard | tricky
# Category: Design / Reservoir sampling

import collections
import random

class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vec = []                                   # holds all values
        self.table = collections.defaultdict(set)       # Maps value -> positions of values
    def insert(self, val):    
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.vec.append(val)
        self.table[val].add(len(self.vec) - 1)
        
        return len(self.table[val]) == 1
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        
        # vec 0 1 1 2 3 2
        # idx 0 1 2 3 4 5
        # Map = 1 : {0, 1}
        #       2 : {3, 5}
        # Suppose we delete 1
        # Steps: 
        #   1. Find any index of 1, and pop that index:
        #         Map 1: {0}
        #             2: {3, 5}
        #   2. Assign last element's value to popped idx.
        # vec 0 1 2 2 3 2
        #         ^ added 2
        #
        #   3. Update last element's value to account for its swap over.
        #   
        #         Map 1: {0}
        #             2: {3, 2}
        #
        #   4. pop back of vec in O(1) time.
        # vec 0 1 2 2 3
        #
        if len(self.table[val]) == 0: return False
        
        rem_idx, last_idx, last_val = self.table[val].pop(), len(self.vec) - 1, self.vec[-1]
        self.vec[rem_idx] = last_val
        
        # MAKE SURE TO ADD BEFORE REMOVE IN CASE rem_idx is last index.
        self.table[last_val].add(rem_idx)
        self.table[last_val].remove(last_idx)
        
        self.vec.pop()
        return True
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        idx = random.randint(0, len(self.vec) - 1)
        return self.vec[idx]
        
