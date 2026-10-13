# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: ListNode | None) -> ListNode | None:
        temp = head
        temp2 = head.next
        arr = []
        while temp2:
            if temp2.val == 0:
                temp.next.val = sum(arr)
                temp.next.next = temp2.next
                arr = []
                temp = temp.next
            arr.append(temp2.val)
            temp2 = temp2.next
        return head.next
