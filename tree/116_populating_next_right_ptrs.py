# Nathan Zhu Wednesday 2:54 pm, Amex building 36th floor
# Leetcode 116 | med | kinda hard without constant extra space
# Category: Binary Tree
# Runtime : O(n)
# Space   : O(1)
# There's a much easier solution, just do a BFS, and connect everything in the BFS.
# 
def connect_tree(root):
    prev, curr = root, None

    while prev and prev.left:
        curr = prev
        while curr:
            # uses new next pointer to connect gap in
            #      A  -> D
            #     / \   / \
            #    E   B  C  F   
            # we know curr has a left and right, cause full tree
            # this line connects E and B
            curr.left.next = curr.right
            # This line connects B to C
            if curr.next: curr.right.next = curr.next.left
            curr = curr.next
        prev = prev.left
    return root