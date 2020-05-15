# Nathan Zhu May 4th, 2020, Stockton, CA,  Meera's birthday was yesterday,  Did above average on the EECS 376 final!! 
# Leetcode 272 | hard | yeah pretty hard
# Category: binary tree

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def make_tree(arr):
    if not arr: return None
    mid = len(arr) // 2
    
    root = TreeNode(arr[mid])
    root.left = make_tree(arr[ :mid])
    root.right = make_tree(arr[mid + 1: ])
    return root



# This is the function
def closestKValues(root, target, k):
    """
    :type root: TreeNode
    :type target: float
    :type k: int
    :rtype: List[int]
    """
    def get_predecessor(stack):
        if not stack: return None
        ret = stack.pop()
        curr = ret.left
        while curr:
            stack.append(curr)
            curr = curr.right
        return ret.val
    
    def get_successor(stack):
        if not stack: return None
        ret = stack.pop()
        curr = ret.right
        while curr:
            stack.append(curr)
            curr = curr.left
        return ret.val
    
    def build_stacks(root, target):
        pre, post = [], []
        while root:
            if root.val < target:
                pre.append(root)
                root = root.right
            else:
                post.append(root)
                root = root.left
        return pre, post
    
    ret = []
    pre, post = build_stacks(root, target)
    l, r = get_predecessor(pre), get_successor(post)
    while k:
        k -= 1
        if l != None and r == None:
            ret.append(l)
            l = get_predecessor(pre)
        elif r != None and l == None:
            ret.append(r)
            r = get_successor(post)
        elif abs(r - target) <= abs(l - target):
            ret.append(r)
            r = get_successor(post)
        else:
            ret.append(l)
            l = get_predecessor(pre)
            
    return ret

if __name__ == "__main__":
    root = make_tree([4, 2, 5, 1, 3])
    print(closestKValues(root, 3.7, 2))