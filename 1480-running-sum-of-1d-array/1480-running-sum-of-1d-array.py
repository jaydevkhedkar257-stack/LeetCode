class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        sum = 0
        for i in range(len(nums)):
            nums[i] += sum
            sum = nums[i]
        return nums