class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]  # loop over-expanded by 1 on each side

        result = ""
        for i in range(len(s)):
            odd = expand(i, i)       # center is a single char
            even = expand(i, i + 1)  # center is between i and i+1
            if len(odd) > len(result):
                result = odd
            if len(even) > len(result):
                result = even
        return result
        