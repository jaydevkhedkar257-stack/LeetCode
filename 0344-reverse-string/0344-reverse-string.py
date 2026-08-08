class Solution:
    def reverseString(self, s: List[str]) -> None:
        size = len(s)
        for i in range(size//2):
            s[i], s[size-(i+1)] = s[size-(i+1)], s[i]
        