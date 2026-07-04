class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node:
                return 0  # height of empty tree

            left = check(node.left)
            if left == -1:
                return -1  # imbalance found below, propagate up

            right = check(node.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1  # this node is unbalanced

            return max(left, right) + 1  # normal height

        return check(root) != -1