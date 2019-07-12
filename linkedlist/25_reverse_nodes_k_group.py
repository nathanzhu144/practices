class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseKGroup(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    # returns from head to tail, returns new head
    def reverse(head, tail):
        if head == tail:
            return head
        newhead = reverse(head.next, tail)
        head.next.next = head
        head.next = None
        return newhead
    
    # Example.
    # k == 3
    # Step 1
    #                v newhead
    # ? -> A -> B -> C -> ?
    #      ^newtail       ^one_after_k
    # Step 2
    #         
    #            newtail   newhead
    #            v         v 
    #       ? -> A <- B <- C   ? 
    #            |             ^one_after_k
    #            v
    #           NULL
    # 
    # Step 3
    #      Connect newhead and newtail
    def helper(node, k):
        newhead, newtail = node, node
        
        for i in range(k - 1):
            if not newhead: return node        # if not k nodes, return current head unmodified
            newhead = newhead.next

        if not newhead: return node            # IMPORTANT NOTE, we need this line
                                               # when k == 1 and k == 2
                                               # at this point, when k == 1 or k == 2.
                                               # When k == 1 the for loop doesn't run, so it is possible that 
                                               # newhead and newtail will be None when we say newhead.next
                                               # When k == 2, the loop runs once, and it is possible newhead ends
                                               # on a None, so newhead.next causes an error

        one_after_k = newhead.next             # we will lose pointer to next k nodes, where we call reverse    
        reverse(node, newhead)
        newtail.next = helper(one_after_k, k)  # step 3, we recurse for next k nodes
        return newhead
        
    return helper(head, k)

## Helpers ##

def print_list(head):
    if not head: return
    print(head.val)
    print_list(head.next)

def make_list(vec):
    if not vec: return None
    curr = ListNode(vec[0])
    curr.next = make_list(vec[1:])
    return curr

if __name__ == "__main__":
    head = make_list([1, 2, 3, 4])
    head = reverseKGroup(head, 3)
    print_list(head)
    # head2 = make_list([1, 2, 3, 4, 4, 3, 2, 1])
    # print(isPalindrome(head2))
    # print_list(head2)
    