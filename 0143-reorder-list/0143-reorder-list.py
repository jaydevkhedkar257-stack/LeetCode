# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if(head is None or head.next is None): return
        stack = []
        temp = head
        while(temp):
            stack.append(temp)
            temp = temp.next
        lenght = len(stack)
        temp = head
        for i in range(lenght//2):
            itm = stack.pop()
            itm.next = temp.next
            temp.next = itm
            temp = temp.next.next
        temp.next = None
         
        