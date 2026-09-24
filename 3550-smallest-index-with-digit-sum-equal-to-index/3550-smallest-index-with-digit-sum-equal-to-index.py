class Solution:
    def smallestIndex(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            temp = nums[i]
            dsum = 0
            while temp:
                dsum += temp%10
                temp = temp//10
            if dsum == i:
                return i
        return -1