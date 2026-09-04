class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i in range(0, len(nums)):
            print(max(nums[0:i+1])-min(nums[i::]), i)
            if k >= max(nums[0:i+1])-min(nums[i::]):
                return i
        return -1