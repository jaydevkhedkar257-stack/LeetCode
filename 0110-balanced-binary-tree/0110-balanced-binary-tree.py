class Solution:
    def dfs(self, root):
        if root is None:
            return 0
        left_height = self.dfs(root.left)
        if left_height == -1:
            return -1
        right_height = self.dfs(root.right)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return 1 + max(left_height, right_height)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root) != -1