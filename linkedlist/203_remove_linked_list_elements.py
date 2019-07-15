# Nathan Zhu 112:53 am Amex Tower 36th floor, Mondau July 8th, 2019
# Leetcode 203 | easy | easy

def remove_linked_list_elements(head, val):
    dummy = TreeNode(0)
    dummy.next = head
    prev, curr = dummy, head

    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = prev.next
        curr = curr.next

    return dummy.next