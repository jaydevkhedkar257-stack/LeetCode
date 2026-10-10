class Solution:
    def minPartitions(self, n: str) -> int:
        n_set = set(n)
        i = 9
        while i:
            if str(i) in n_set:
                return i
            i -= 1
        return i