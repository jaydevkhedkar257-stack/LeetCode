# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        
        # Traverse until the current node or the next node is None
        while curr and curr.next:
            # If a duplicate is found, bypass the next node
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            # Otherwise, just move the pointer forward safely
            else:
                curr = curr.next
                
        return head