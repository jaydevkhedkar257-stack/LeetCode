class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if(nums[0] > target):
            return 0
        elif(nums[len(nums)-1] < target):
            return len(nums)
        i, j = 0, len(nums)-1
        sugggested_index = i
        while(i <= j):
            mid = i + ((j-i)//2)
            if(nums[mid] == target):
                return mid
            elif(nums[mid] > target):
                j = mid - 1
            else:
                sugggested_index = mid
                i = mid + 1
        return sugggested_index + 1