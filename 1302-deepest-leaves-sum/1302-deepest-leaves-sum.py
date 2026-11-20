# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode | None) -> int:        
        q = deque([root])
        while q:
            deepestLeaveSum = 0
            for i in range(len(q)):
                element = q.popleft()
                deepestLeaveSum += element.val
                if element.left:
                    q.append(element.left)
                if element.right:
                    q.append(element.right)

        return deepestLeaveSum
            
