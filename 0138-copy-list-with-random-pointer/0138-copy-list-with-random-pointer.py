"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if(head is None): return head
        temp1 = head
        dummy = Node(head.val)
        temp2 = dummy
        bind = {}
        bind_val = {}
        while(temp1):
            bind[temp1] = temp2
            bind_val[temp1.val] = temp2.val
            temp2.next = Node(temp1.next.val) if temp1.next is not None else None
            temp2 = temp2.next
            temp1 = temp1.next
        temp1 = head
        # print(bind_val)
        while(temp1):
            if(temp1.random in bind):
                bind[temp1].random = bind[temp1.random] #temp2.random
            else:
                bind[temp1].random = None
            temp1 = temp1.next
        return dummy