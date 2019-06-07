class Node:
    def __init__(self, val_in):
        self.val = val_in
        self.next = None

    
    
def copy(node_in):
    dummy = Node(0)
    head = dummy
    curr = dummy

    while node_in is not None:
        curr.next = Node(node_in.val)
        curr = curr.next
        node_in = node_in.next

    return head.next

## Helper functions ##
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
    





