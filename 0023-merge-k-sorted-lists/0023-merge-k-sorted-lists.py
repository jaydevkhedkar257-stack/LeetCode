# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        while(len(lists) > 1):
            dummy = ListNode(0)
            temp3 = dummy
            temp1 = lists[0]
            temp2 = lists[1]
            while(temp1 and temp2):
                if(temp1.val > temp2.val):
                    temp3.next = temp2
                    temp3 = temp3.next
                    temp2 = temp2.next
                else:
                    temp3.next = temp1
                    temp3 = temp3.next
                    temp1 = temp1.next
            if(temp1):
                temp3.next = temp1
            else:
                temp3.next = temp2
            lists.pop(0)
            lists.pop(0)
            lists.append(dummy.next)
        return lists[0]