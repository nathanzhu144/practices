#  Nathan Zhu, 12:09 am Friday July 12th, 2019, New York, 55 John Street.  
#  Leetcode 988 | medium | not too bad, easier emd
# 
#  
# Problem: 
#
# Given the root of a binary tree, each node has a value from 0 to 25 representing the letters 'a' to 'z': 
# a value of 0 represents 'a', a value of 1 represents 'b', and so on.
#
# Find the lexicographically smallest string that starts at a leaf of this tree and ends at the root.
#
#  Solution:
#
#  First, note that a divide and conquer approach cannot work.  Since we are looking for the smallest
#  word from leaf, it is obvious that there is no way to tell which word is bigger starting from the
#  back fo two words.  Therefore, we need to do a DFS of every possible word to see which one is biggest.
# 
#          A
#     A        B
#  C     Z      A 
# 
def smallest_from_leaf(root):
    def helper(root, curr_path, returned):
        if not root: return
        
        # this should convert 0 -> a and so on
        # prob hardest part of question, lol
        curr_path.append(chr(ord('a') + root.val))

        # we have reached leaf node, add it to returned if returned is empty or choose lesser of two
        if not root.left and not root.right: 
            if not returned: returned.append("".join(curr_path[::-1]))
            else:
                returned[0] = min("".join(curr_path[::-1]), returned[0])
            return

        # we recurse on left or right, as either we have a left or we have a right or both
        helper(root.left, curr_path[:], returned)
        helper(root.right, curr_path[:], returned)
        
    ret = list()
    helper(root, list(), ret)
    return ret[0]