class Solution:
    def minElement(self, nums: List[int]) -> int:
        sum = 0
        min_sum = float('inf')
        for i in range(len(nums)):
            temp = nums[i]
            while temp:
                sum += (temp%10)
                temp = temp//10
            nums[i] = sum
            min_sum = min(sum, min_sum)
            sum = 0
        return min_sum