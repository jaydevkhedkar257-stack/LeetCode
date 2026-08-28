# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while temp.next:
            temp2 = temp.next
            temp.next = ListNode(self.gcd(temp.val, temp2.val), temp2)
            temp = temp2
        return head