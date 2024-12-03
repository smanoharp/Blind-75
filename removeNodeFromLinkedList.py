# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head

        1# move fast pointer n steps
        for i in range(n):
            fast = fast.next

        #edge case when n is length, fast will be none
        if not fast:
            return head.next

        2# move fast and slow pointers
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        return head