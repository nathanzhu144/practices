Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5



public ListNode insertionSortList(ListNode head) {
		if( head == null ){
			return head;
		}
		
		ListNode helper = new ListNode(0); //new starter of the sorted list
		ListNode cur = head; //the node will be inserted
		ListNode pre = helper; //insert node between pre and pre.next
		ListNode next = null; //the next node will be inserted
		//not the end of input list
		while( cur != null ){
			next = cur.next;
			//find the right place to insert
			while( pre.next != null && pre.next.val < cur.val ){
				pre = pre.next;
			}
			//insert between pre and pre.next
			cur.next = pre.next;
			pre.next = cur;
			pre = helper;
			cur = next;
		}
		
		return helper.next;
	}
}
# DUMMY -1 -> 5 -> 3 -> 4 -> 0
#  ^pre ^curr 
#  
# DUMMY -1 -> 5 -> 3 -> 4 -> 0
#        ^pre ^curr
#  
def insertion_sort(head):
    if not head: return None         # no list is not sorted

    dummy = ListNode(float("-inf"))
    dummy.next = head
    pre = dummy
    curr = head

    while curr:
        nextptr = curr.next

        while pre.next and pre.val < pre.next.val:
            pre = curr
            curr = curr.next

        

        


