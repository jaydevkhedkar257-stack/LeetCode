class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        presum = [0]*len(nums)
        postsum = [0]*len(nums)
        res = [0]*len(nums)
        for i in range(1, len(nums)):
            presum[i] = presum[i-1] + nums[i-1]
        for j in range(len(nums)-2,-1,-1):
            postsum[j] = postsum[j+1] + nums[j+1]
        for k in range(len(nums)):
            res[k] = abs(presum[k] - postsum[k])
        return res