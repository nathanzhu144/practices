# Nathan Zhu, Flight from Chicago to New York, 8:00 pm
# Leetcode 148 | medium | I think not too bad, medium question
# 
def merge_sort_list(head):
    # recursive list merging
    def merge(n1, n2):
        if not n1 or not n2: return n1 if n1 else n2
        if n1.val < n2.val:
            n1.next = merge(n1.next, n2)
            return n1
        else:
            n2.next = merge(n1, n2.next)
            return n2

    def sort_list(head):
        # Base cases, cases of size 0 LL or size 1 LL
        if not head or not head.next: return head
        
        # We want slow to be middle of LL, and if LL is even, will point to right middle
        # Pre should be node before slow and if LL is even, will point to right middle
        slow, fast, pre = head, head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        # pre points to pointer right before middle of LL
        # we split the linked list into two
        pre.next = None

        # We divide and conquer on left and right
        sort_left = sort_list(head)
        sort_right = sort_list(pre)

        return merge(sort_left, sort_right)
        

