# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if(p is None and q is None):
        #     return root
        # if(p is None or q is None):
        #     return p or q
        if(p.val > q.val):
            p, q = q, p
        # def ischild(root, child):
        #     if(root is None):
        #         return False
        #     return root.val == child.val or ischild(root.left, child) or ischild(root.right, child)
        # if(ischild(p, q)):
        #     return p
        # elif(ischild(q, p)):
        #     return q
        curr = root
        while(curr.val < p.val or curr.val > q.val):
            if(curr.val < p.val):
                curr = curr.right
            else:
                curr = curr.left
        return curr