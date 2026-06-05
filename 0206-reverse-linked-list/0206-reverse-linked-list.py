# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        stack = []
        temp = head
        while(temp != None):
            stack.append(temp)
            temp = temp.next
        temp1 = stack[-1]
        temp2 = stack[-1]
        while(stack):
            temp1.next = stack.pop()
            temp1 = temp1.next
        temp1.next = None
        return temp2