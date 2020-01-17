#  Nathan Zhu
#  Amex Tower, New York, NY, 36th floor
#  So, I've been struggling on the iterative version for so long.. 
#  The recursive way makes so much more sense, haha
#
#  NOTE: iter is damn cool

import collections

##  In this version, we convert a binary tree to its preorder, but in the process
#   we add a "#" for each nullptr
#
# from binary tree -> preorder string
def serialize_rec(root):
    def helper(root):
        if root:
            serialized.append(str(root.val))
            helper(root.left)
            helper(root.right)
        else:
            serialized.append("#")
    serialized = []
    helper(root)
    return ' '.join(serialized)

# from preorder string to binary tree
def deserialize_rec(data):
    """Decodes your encoded data to tree.
    
    :type data: str
    :rtype: TreeNode
    """
    def helper():
        curr = next(str_iter)
        if curr == "#": return None
        node = TreeNode(int(curr))
        node.left = helper()     # note no arguments to helper()
        node.right = helper()
        return node
    str_iter = iter(data.split(" "))  # iterators are cool...
    return helper()

#####
#     Unfinished...
##### 

# input treenode root
# output string
def serialize(root):
    if not root: return ""
    res, q = list(), collections.deque([root])
    while q:
        curr = q.pop(0)  #popleft
        if curr:
            q.append(curr.left)
            q.append(curr.right)
        res.append(str(curr.val) if curr else '#')
    return ','.join(res)

# input string
# output tree
def deseralize(str):
    if not str: return None
    
    str_list = str.split(",")
    returned = TreeNode(str_list[0])
    q = collections.deque(returned)

    for i in range(1, len(str_list)):
        curr = q.popright()
        if str_list[i] != "#":
            temp = TreeNode(str_list[i])
            curr.left = temp
            q.append(temp)
        if str_list[i] != "#":
            temp = TreeNode(str_list[i])
            curr.right = temp
            q.append(temp)

    return returned
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/74259/Recursive-preorder-Python-and-C%2B%2B-O(n)




























def deseralize(str):
    if not string: return None
    # convert string to a list
    tree_list = []
    q = collections.deque()
    
    root = TreeNode[tree_list(0)]
    q.push(root)
    counter = 1

    while counter < len(tree_list):
        curr = q.pop(0)
        if tree_list[index] != "#":
            new = TreeNode(int(tree_list[index]))
            curr.left = new
            index += 1
            q.push(new)
        if tree_list[index] != "#":
            new = TreeNode(int(tree_list[index]))
            curr.right = new
            index += 1
            q.push(new)
        
        



        
