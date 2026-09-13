class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                res.insert(0, 0)
            else:
                res.append(1)
        return res