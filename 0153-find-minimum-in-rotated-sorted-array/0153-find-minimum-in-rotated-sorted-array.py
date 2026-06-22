class Solution:
    def findMin(self, nums: List[int]) -> int:
        if(sorted(nums) == nums): return nums[0]
        i = 0
        step_size = 1
        while(i+step_size < len(nums) and nums[i] < nums[i+step_size]):
            i = i + step_size
            step_size = 2*step_size

        j = len(nums)-1
        while(i <= j):
            mid = i + ((j-i)//2)
            if(nums[mid] > nums[i]):
                i = mid
            elif(nums[mid] < nums[j]):
                j = mid
            else:
                return nums[(i+1)%len(nums)]