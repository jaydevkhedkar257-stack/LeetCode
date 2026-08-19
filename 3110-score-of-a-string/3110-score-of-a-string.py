class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        prev = s[0]
        for i in s:
            res += abs(ord(i)-ord(prev))
            prev = i
        return res