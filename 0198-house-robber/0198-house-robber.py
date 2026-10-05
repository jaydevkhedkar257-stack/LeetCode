class Solution:
    def rob(self, nums: list[int]) -> int:
        i = len(nums) - 3
        while i >= 0:
            nums[i] += max(nums[i+2:len(nums)])
            i -= 1

        return max(nums[0],nums[1]) if len(nums) > 3 else max(nums)