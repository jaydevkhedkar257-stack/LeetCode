class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        i = 0
        count_pair = 0

        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] < target:
                    count_pair += 1
                j += 1
            i += 1
        
        return count_pair
