# Nathan Zhu Feb 16th, 2020.  Feels strage being 22.  Had my birthday yesterday at bdubs.  Time goes by and you don't know tice y'know?
# Leetcode 515 | medium | easy
# Category: btree 

import collections
def largest_val(root):
    table = collections.defaultdict(lambda: float('-inf'))
    
    def helper(root, level):
        if not root: return
        
        table[level] = max(table[level], root.val)
        
        helper(root.left, level + 1)
        helper(root.right, level + 1)
    
    helper(root, 0)
    ret = []
    i = 0
    while True:
        if i not in table: break
        ret.append(table[i])
        i += 1
        
    return ret
