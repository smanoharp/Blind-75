# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #1 find the middle
        if not head: return None

        slow, fast = head, head
        while(fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next

        #reverse 2nd list
        prev = None
        curr = slow.next
        while(curr != None):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        slow.next = None

        #Merge 2 lists
        head1 = head
        head2 = prev
        while(head1 and head2):
            nxt1 = head1.next
            nxt2 = head2.next

            head1.next = head2
            head1 = nxt1

            head2.next = head1
            head2 = nxt2




