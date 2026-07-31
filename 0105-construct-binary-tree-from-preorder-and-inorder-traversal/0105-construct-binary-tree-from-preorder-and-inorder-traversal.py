class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None

        root = TreeNode(preorder[0])
        pivot = inorder.index(root.val)

        Lsubtree = inorder[:pivot]
        Rsubtree = inorder[pivot+1:]

        root.left = self.buildTree(preorder[1:1+len(Lsubtree)], Lsubtree)
        root.right = self.buildTree(preorder[1+len(Lsubtree):], Rsubtree)
        return root