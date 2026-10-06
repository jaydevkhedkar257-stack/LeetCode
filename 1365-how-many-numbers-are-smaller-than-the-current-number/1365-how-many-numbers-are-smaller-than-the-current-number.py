class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        res = [0]*len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                elif nums[i] > nums[j]:
                    res[i] += 1
        return res