# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        q = deque()
        def bfs(root, q):
            q.append(root)
            res = []
            while q:
                res.append(q[-1].val)
                for i in range(len(q)):
                    element = q.popleft()
                    if(element):
                        if(element.left):
                            q.append(element.left)
                        if(element.right):
                            q.append(element.right)
            return res
        return bfs(root, q)
                
        