
# 
# NOTE: you can swap a doubly linked list in O(1) time by switching the head and the tail pointers
#
#  def reverse

class Node:
    def __init__(self, val_in):
        self.val = val_in
        self.next = None

# Reverse linked list function
def reverseListRecursive(head):
    def helper(node):
        if node is None or node.next is None:
            return node
        
        head = helper(node.next)  # returns hard
        node.next.next = node
        node.next = None
        return head
    
    return helper(head)

def reverseListIterative(head):
    newhead = None
    curr = head
    next = head

    while curr is not None:
        next = head.next
        curr.next = newhead
        newhead = curr
        curr = next

    return newhead


######################
#  Helper functions ##
######################
def printlist(node_in):
    while node_in is not None:
        print(node_in.val)
        node_in = node_in.next

def makelist(list_in):
    dummyhead = Node(float('-inf'))
    curr = dummyhead

    for i in list_in:
        curr.next = Node(i)
        curr = curr.next

    return dummyhead.next

if __name__ == "__main__":
    printlist(reverseListIterative(makelist([1, 2, 3, 4, 5])))
    #printlist(reverseListRecursive(makelist([1, 2, 3, 4, 5])))
    