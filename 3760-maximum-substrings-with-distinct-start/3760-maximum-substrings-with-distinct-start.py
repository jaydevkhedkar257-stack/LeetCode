class Solution:
    def maxDistinct(self, s: str) -> int:
        # start_letter = set()
        # count = 0
        # for i in s:
        #     if i not in start_letter:
        #         count += 1
        #         start_letter.add(i)
        # return count
        return len(set(s))