class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not (list1 or list2): return None
        elif not list1: return list2
        elif not list2: return list1

        temp0 = list1 if list1.val <= list2.val else list2
        temp1 = list2 if list1.val <= list2.val else list1
        newhead = temp0

        while temp0 and temp1:
            if temp0.next is None:
                temp0.next = temp1
                break
            if temp1.val <= temp0.next.val:
                temp3 = temp1.next
                temp1.next = temp0.next
                temp0.next = temp1
                temp0 = temp0.next
                temp1 = temp3
            else:
                temp0 = temp0.next

        return newhead