# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubroot(self, root, subroot, troots):
        if(root is None):
            return
        if(root.val == subroot.val):
            troots.append(root)
        return self.isSubroot(root.left,subroot,troots) or self.isSubroot(root.right,subroot,troots)
    
    def isSameTree(self, troot, subRoot):
        if(subRoot is None and troot is None):
            return True
        if(subRoot is None and troot is not None):
            return False
        if(subRoot is not None and troot is None):
            return False 
        # print(troot.val, subRoot.val)
        return subRoot.val == troot.val and self.isSameTree(troot.left, subRoot.left) and self.isSameTree(troot.right, subRoot.right)
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        troots = []
        self.isSubroot(root, subRoot, troots)
        # print(troot.val)
        res = False
        for i in troots:
            res = res or self.isSameTree(i, subRoot)
        return res