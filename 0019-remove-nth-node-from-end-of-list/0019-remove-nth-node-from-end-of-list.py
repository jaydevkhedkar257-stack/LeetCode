# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if(head is None or head.next is None):
            return None

        temp = head
        length = 0
        while(temp is not None):
            temp = temp.next
            length += 1
        if(length == n): return head.next
        increement = n+1
        slow, fast = head, head
        while(fast is not None and increement > 0):
            fast = fast.next
            increement -= 1
        while(fast is not None):
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
        