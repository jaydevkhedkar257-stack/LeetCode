class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        j = len(s)-1
        while(s[j] == " "):
            j -= 1
        end = j
        while(j >= 0 and s[j] != " "):
            j -= 1
        start = j
        return end-start