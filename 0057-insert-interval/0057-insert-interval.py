class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        nums = intervals.copy()

        i, j = 0, len(nums)
        while i < j:
            mid = (i + j) // 2
            if nums[mid][0] < newInterval[0]:
                i = mid + 1
            else:
                j = mid
        nums.insert(i, newInterval)  
        
        i = 0
        # print(nums)
        while i < len(nums) - 1:
            if nums[i][0] <= nums[i+1][1] and nums[i][1] >= nums[i+1][0]:
                element1 = nums.pop(i)
                element2 = nums.pop(i)
                start = element1[0]
                end = element2[1] if element2[1] > element1[1] else element1[1]
                nums.insert(i, [start, end])
                i -= 1
            # print(nums, i)
            i += 1
        return nums