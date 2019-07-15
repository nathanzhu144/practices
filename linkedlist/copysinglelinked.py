class Node:
    def __init__(self, val_in):
        self.val = val_in
        self.next = None

    
#To see explanation, see explanations folder for copysinglelinked
def copy(node_in):
    dummy = Node(0)
    head = dummy
    curr = dummy

    while node_in is not None:
        curr.next = Node(node_in.val)
        curr = curr.next
        node_in = node_in.next

    return head.next

#This is really elegant and clean. It is too simple for a proper explanation, I think,
#but the idea is that you copy a node one by one, and you set the next equal to the processing
#of the rest of the linked list
def copy_recursive(node_in):
    if node_in is None:
        return node_in

    newnode = Node(node_in.val)
    newnode.next = copy_recursive(node_in.next)

    return newnode

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
    printlist(copy(makelist([1, 2, 3, 4, 5])))
    printlist(copy_recursive(makelist([1, 2, 3, 4, 5])))
    





