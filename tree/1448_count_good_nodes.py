# Nathan Zhu May 16th, 2020 Stockton, CA During Biweekly contest
# Leetcode 1448 | medium | easy
# Category: tree
# Did this during the contest.  I did damn well, and messed up so damn bad on this contest.  I had two wrong answers on this trash problem lol bc I Was 
# being silly with out-of-bounds checking.  I also had 2 TLEs for the 4th DP problem, the first because I didn't memoize (even after making the table lol), and the second because I
# didn't see why the first one TLEd.  
# 
# Also, I finished the contest in 37 min.  I was so proud of myself.  
#
# I hit position 181 just as I finished, but it went down to 450.  I feel that I'm getting better.  I guess today I just realized how good I was getting.
# For a game like Starcraft, top 200 is rougly the beginning of GM.  Now, obviously my performance isn't consistently in top 400, but my lowest ranking is usually
# ~2000, which is still top 5%.  Anyway, I am getting there.
#

def goodNodes(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    def helper(root, max_val):
        if not root: return 0
        
        ret = 0
        if root.val >= max_val: ret += 1
        
        return ret + helper(root.left, max(max_val, root.val)) + helper(root.right, max(max_val, root.val))
    
    return helper(root, float('-inf'))
        