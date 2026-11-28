class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        res = []
        for i in range(0,len(nums),2):
            f = nums[i]
            v = nums[i+1]
            res += [v]*f
        return res