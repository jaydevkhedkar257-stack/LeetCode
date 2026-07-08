# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, stack):
        if(root is None):
            stack.append(root)
            return 
        stack.append(root.val)
        self.dfs(root.left, stack)
        self.dfs(root.right, stack)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack1 = []
        stack2 = []
        self.dfs(p, stack1)
        self.dfs(q, stack2)
        print(stack1, stack2)
        return stack1 == stack2
