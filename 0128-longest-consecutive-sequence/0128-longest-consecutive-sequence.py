class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)  # O(n)
        max_count = 0

        for num in num_set:
            # Only start counting from the beginning of a sequence
            if num - 1 not in num_set:
                count = 1
                while num + count in num_set:
                    count += 1
                max_count = max(max_count, count)

        return max_count