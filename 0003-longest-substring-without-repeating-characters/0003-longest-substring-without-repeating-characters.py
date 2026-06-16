class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        i = 0
        count = 0

        for j in range(len(s)):
            while s[j] in char_set:
                char_set.remove(s[i])
                i += 1
            char_set.add(s[j])
            count = max(count, j - i + 1)

        return count