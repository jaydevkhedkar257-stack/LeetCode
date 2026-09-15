"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visit = defaultdict()

        def dfs(origin):
            if origin is None:
                return

            temp = Node(origin.val)
            visit[origin] = temp
            curr = []
            for i in origin.neighbors:
                if i in visit:
                    curr.append(visit[i])
                    continue
                curr.append(dfs(i))
            
            temp.neighbors = curr
            return temp

        return dfs(node)
