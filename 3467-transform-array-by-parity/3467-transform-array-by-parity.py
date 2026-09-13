class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] % 2
        nums.sort()
        return nums