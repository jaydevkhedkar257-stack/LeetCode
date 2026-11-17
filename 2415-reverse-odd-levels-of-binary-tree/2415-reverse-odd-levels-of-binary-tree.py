# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: TreeNode | None) -> TreeNode | None:
        q = deque()
        q.append(root)
        ctr = 0
        while q:
            temp2 = []
            for _ in range(len(q)):
                element = q.popleft()
                temp2.append(element)
                if element.left:
                    q.append(element.left)
                if element.right:
                    q.append(element.right)
            if ctr%2 == 1:
                curr = [element.val for element in temp2]
                curr = curr[::-1]
                for i in range(len(curr)):
                    temp2[i].val = curr[i]
            ctr += 1
                
        return root
            