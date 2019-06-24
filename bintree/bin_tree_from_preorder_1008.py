#  Nathan Zhu June 23rd, 2019, American Express Building, 10:30 pm
# 
#  Idea is simple.
#  1. First item in preorder list is the root to be considered.
#  2. For next item in preorder list, there are 2 cases to consider:
#      If value is less than last item in stack, it is the left child of last item.
#      If value is greater than last item in stack, pop it.
#  3. The last popped item will be the parent and the item will be the right child of the parent.

import collections

def preorder_arr_to_bintree(arr):
    if not arr: return None
    
    root = TreeNode(arr[0])
    stack = collections.deque([root])

    # We iterate from 1 cause we have root in stack already
    for val in arr[1:]:
        curr = None
        new_node = TreeNode(val)
        # this is case where new node is right child of last popped item
        if stack and val > stack[-1].val:
            while stack and val > stack[-1].val:
                curr = stack.pop()
            curr.right = new_node
        # this is case where new node is left child of node on top of stack
        else:
            curr = stack[-1]
            curr.left = new_node
        stack.append(new_node)

    return root

                
            