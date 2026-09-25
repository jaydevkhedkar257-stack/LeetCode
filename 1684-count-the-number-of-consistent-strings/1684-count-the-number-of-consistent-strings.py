class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        hash_allow = set(allowed)
        count = 0
        for i in words:
            if set(i) - hash_allow == set():
                count += 1
        return count