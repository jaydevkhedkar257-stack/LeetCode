# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2
        dummy = ListNode(0)
        temp3 = dummy
        carry = 0

        while(temp1 and temp2):
            temp3.next = ListNode((temp1.val + temp2.val + carry)%10)
            carry = (temp1.val + temp2.val + carry)//10
            temp3 = temp3.next
            temp2 = temp2.next
            temp1 = temp1.next


        while(temp1):
            temp3.next = ListNode((temp1.val + carry)%10)
            carry = (temp1.val + carry)//10
            temp3 = temp3.next
            temp1 = temp1.next
        while(temp2):
            temp3.next = ListNode((temp2.val + carry)%10)
            carry = (temp2.val + carry)//10
            temp3 = temp3.next
            temp2 = temp2.next
        while(carry != 0):
            temp3.next = ListNode(carry%10)
            carry = carry//10
            temp3 = temp3.next
        return dummy.next
        

