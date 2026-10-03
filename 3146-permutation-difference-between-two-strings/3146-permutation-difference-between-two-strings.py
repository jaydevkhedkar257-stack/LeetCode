class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        sMap = defaultdict(int)
        tMap = defaultdict(int)

        for i in range(len(s)):
            sMap[s[i]] = i
            tMap[t[i]] = i

        perm_diff = 0
        for j in sMap:
            perm_diff += abs(sMap[j] - tMap[j])
        
        return perm_diff
            