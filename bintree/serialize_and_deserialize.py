import collections

# input treenode root
# output string
def serialize(root):
    if not root: return ""
    res, q = list(), collections.deque([root])
    while q:
        curr = q.pop(0)  #popleft
        if curr:
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
            res.append(curr.val)
        else:
            res.append("#")
    return ','.join(res)

# input string
# output tree
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
        
        



        
