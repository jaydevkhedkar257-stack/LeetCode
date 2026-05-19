class Solution(object):
    def twoSum(self, nums, target):
        prevMap = {}
        for i in range(0,len(nums)):
            if((target - nums[i]) in prevMap):
                return [i,prevMap[target - nums[i]]]
            else:
                prevMap[nums[i]] = i
        return