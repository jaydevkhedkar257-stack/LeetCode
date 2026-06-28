class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums)-1
        count = 0
        while(i <= j):
            if(nums[j] == val):
                j -= 1
            elif(nums[i] == val):
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
                count += 1
            else:
                i += 1
                count += 1
        return count