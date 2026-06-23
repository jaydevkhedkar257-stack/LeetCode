from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        
        while i <= j:
            mid = i + ((j - i) // 2)
            
            if nums[mid] == target:
                return mid
            
            # Step 1: Check if the left half is normally sorted
            if nums[i] <= nums[mid]:
                # Step 2: Check if target lies within this sorted left half
                if nums[i] <= target < nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
            # Step 3: Otherwise, the right half must be sorted
            else:
                # Step 4: Check if target lies within this sorted right half
                if nums[mid] < target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1
                    
        return -1