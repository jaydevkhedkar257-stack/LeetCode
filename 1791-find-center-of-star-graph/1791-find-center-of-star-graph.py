class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        A = set(edges[0])
        B = set(edges[1])
        for i in B.intersection(A):
            return i