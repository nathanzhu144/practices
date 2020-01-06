import collections

# def selectPackages(truckSpace, packagesSpace):
#     truckSpace = 30
#     target = truckSpace - 30
#     packagesSpace = [0, 0]
    
#     table = dict()
#     largest_pkg = 0
#     ret = [-1, -1]
#     for i in range(len(packagesSpace)):
#         curr_val = packagesSpace[i]
        
#         # We have found a valid pair.
#         if target - curr_val in table and table[target - curr_val] != i:
#             biggest_num = max(target - curr_val, curr_val)
#             if biggest_num > largest_pkg:
#                 largest_pkg = biggest_num
#                 ret = [table[target - curr_val], i]
                
#         table[curr_val] = i
                
#     return ret
def pathSum(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: int
    """
    table = collections.defaultdict(int)
    table[0] = 1
    
    def helper(root, table, currsum, target):
        if not root: return 0
        
        ret = 0
        currsum += root.val
        
        if target - currsum in table:
            ret = table[target - currsum]
        
        table[currsum] += 1
        
        ret += (helper(root.left, table, currsum, target) + helper(root.right, table, currsum, target))
        return ret
        
    ret = helper(root, table, 0, sum)
    
    
    return ret
            
if __name__ == "__main__":
    selectPackages(30, [0, 0])