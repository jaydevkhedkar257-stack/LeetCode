# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        def build_bst(left: int, right: int) -> TreeNode | None:
            if left > right:
                return None
            
            # Choose middle element
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            
            # Build left and right subtrees recursively
            root.left = build_bst(left, mid - 1)
            root.right = build_bst(mid + 1, right)
            
            return root

        return build_bst(0, len(nums) - 1)