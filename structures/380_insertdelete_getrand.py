# Nathan Zhu Tuesday, July 23rd, 2019, 11:50 am, Overlooking Hudson River Amex  Building
# Leetcode 380 | medium | ehh, hard?, not much code, but a lotta edge cases

# Data stuctures
# 1. We have a list to store all the numbers in set.
# 2. We have a hash table: num -> pos in vector
#  

# Observations #
# Normally, removing from middle or front of a vector is an O(N) operation.  
# 
# Also, finding an element in a vector is an O(N) vector if it isn't sorted.

# So, how do we remove in O(1) time?
# 
# [?, ?, ?, 2, ?, ?, 8]
# self.pos = {{val 2 -> pos 3}.
#              val 8 -> pos 7}
#
# Let's say we want to remove 2.  Finding its position in the list is O(1) time w self.pos hash table.
# 
# Then we swap the last element of set to where position of 2 is, and delete the pair {val 2 -> pos 3} like this:
# 
# [?, ?, ?, 8, ?, ?, 8]
# self.pos = {   [deleted]
#              val 8 -> pos 7}}
#
# Last, update the last element's self.pos mapping, and pop the last element off the end of the list.
# 
# [?, ?, ?, 8, ?, ?]
# self.pos = {   [deleted]
#              val 8 -> pos 3}}
#
# Getting random in O(1) time is trivial.
# Inserting in O(1) is also trivial.


# Followup: What if we wanted to store duplicate elements?
#           with getRandom will have a proportionally higher chance of grabbing a duplicate element.
#
#           Easy, we can change self.pos to a hash table of (int) -> list(int)
#           self.pos would map to ALL indices of val, and whenever we want to remove
#           an instance of a val, we can just check if the list is empty; if it is not 
#           empty, we remove the instance of val at the first index.
#
#           Before
#           [?, 2, ?, ?, 2, 2, SWAP]
#           self.pos = {{2} : [1, 4, 5]}
#           
#           After
#           [?, SWAP, ?, ?, 2, 2]         [2] <- removed from end
#           self.pos = {{2} : [4, 5]}
## Observations #
# Normally, removing from middle or front of a vector is an O(N) operation.  
# 
# Also, finding an element in a vector is an O(N) vector if it isn't sorted.


# Followup: What if we wanted to store duplicate elements?
#           with getRandom will have a proportionally higher chance of grabbing a duplicate element.
#
#           Easy, we can change self.pos to a hash table of (int) -> list(int)
#           self.pos would map to ALL indices of val, and whenever we want to remove
#           an instance of a val, we can just check if the list is empty; if it is not 
#           empty, we remove the instance of val at the first index.
#
#           Before
#           [?, 2, ?, ?, 2, 2, SWAP]
#           self.pos = {{2} : [1, 4, 5]}
#           
#           After
#           [?, SWAP, ?, ?, 2, 2]         [2] <- removed from end
#           self.pos = {{2} : [4, 5]}
#
from random import randrange

class RandomizedSet(object):

    def __init__(self):
        # Data structures #
        # self.nums   (stores all vals)
        # self.pos    val -> positions
        self.nums, self.pos = [], {}

    # 1. We check if val is in positions
    # 2. Then, we create mapping, mapping val -> its position at end of list
    # 3. We append val to self.pos
    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.pos: return False
        
        self.pos[val] = len(self.nums)
        self.nums.append(val)
        return True

    # Step 1
    # [?, ?, ?, 2, ?, ?, 8]
    #           ^ remove_idx 
    #                    ^ last_el_val == 8
    # self.pos = {{2} : [3],
    #             {6} : [8]}
    # Step 2
    # [?, ?, ?, 8, ?, ?, 8]
    #           ^ remove_idx 
    #                    ^ last_el_val == 8
    #  self.pos = {{2} : [3],
    #              {6} : [8]}
    #
    # Step 3
    # [?, ?, ?, 8, ?, ?, 8]
    #           ^ remove_idx 
    #                    ^ last_el_val == 8
    #  self.pos = {{6} : [3]}
    #
    # 0. We check to see if val is not in positions
    # 1. We find index of remove_idx and last_el
    # 2. We overwrite val stored at remove_idx; we are deleting it, and don't need it anymore
    # 3. 
    #     NOTE: ORDER IS EXTREMELY IMPORTANT, IF A AND B ARE SWITCHED, THERE'S A BUG IF WE 
    #           REMOVE LAST ELEMENT FROM LIST.  Because last_el_val is at remove_idx,
    #           after we remove self.pos[last_el_val], we accidentally re-create it with self.pos[val].
    #
    #     a) We change self.pos[last_el_val] to its new place,
    #     b) We remove mapping of self.pos[val]
    #
    # 4. We pop redundant last_el_val off end of self.nums.
    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            #Step 1
            remove_idx, last_el_val = self.pos[val], self.nums[-1]
            
            #Step 2
            self.nums[remove_idx] = last_el_val
            
            #Step 3
            self.pos[last_el_val] = remove_idx
            del self.pos[val]
            
            #Step 4
            self.nums.pop()
            return True
        return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.nums[random.randrange(len(self.nums))]