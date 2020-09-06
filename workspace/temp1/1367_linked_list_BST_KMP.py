# Nathan Zhu, June 3rd, 2020 Stockton, CA.  Been a year and a day since the beginning!  Old Nathan would be proud.
# Leetcode 1367 | medium | medium
# Category: KMP
# Dang this question is kinda cool man, I wasn't at all thinking of doing KMP on a binary tree to get an min(N, K)
# algorithm where N is number of nodes in the tree and K is length of linked list from head.
# 


def isSubPath(self, head, root):
    """
    :type head: ListNode
    :type root: TreeNode
    :rtype: bool
    """
    def make_kmp(arr):
        N = len(arr)
        ret = [0] * N
        i, j = 1, 0
        
        while i < N:
            if arr[i] == arr[j]:
                ret[i] = j + 1
                i += 1
                j += 1
            else:
                if j > 0: j = ret[j - 1]
                else: i += 1
        return ret
    
    def helper(kmparr, head, i):
        if i == len(kmparr): return True
        if not head: return False
        
        while i > 0 and head.val != arr[i]:
            i = kmparr[i - 1]
        if head.val == arr[i]: i += 1
        return helper(kmparr, head.left, i) or helper(kmparr, head.right, i)
        
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
        
    kmparr = make_kmp(arr)
    return helper(kmparr, root, 0)
    