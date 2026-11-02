class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        res = [0] * len(nums)
        glob_max = 0
        for i in range(len(nums)-1, -1, -1):
            max_step = 0
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    max_step = max(max_step, res[j])
            res[i] = max_step + 1
            glob_max = max(glob_max, res[i])
        return glob_max
                
