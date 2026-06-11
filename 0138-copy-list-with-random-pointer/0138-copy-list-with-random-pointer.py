class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        bind = {}  # original node -> copy node
        
        # First pass: create all copy nodes
        cur = head
        while cur:
            bind[cur] = Node(cur.val)
            cur = cur.next
        
        # Second pass: wire next and random
        cur = head
        while cur:
            bind[cur].next = bind[cur.next] if cur.next else None
            bind[cur].random = bind[cur.random] if cur.random else None
            cur = cur.next
        
        return bind[head]