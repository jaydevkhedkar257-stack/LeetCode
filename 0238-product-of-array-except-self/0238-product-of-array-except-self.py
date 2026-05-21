class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        if(len(nums) == 1): return nums[0]

        preprod = [1]*len(nums)
        postprod = [1]*len(nums)
        result = [1]*len(nums)
        index = 0

        for i in range(0, len(nums)):
            if(i == 0):
                preprod[i] = nums[i]
            else:
                preprod[i] = preprod[index]*nums[i]
                index = i
        
        index = len(nums)-1

        for i in range(len(nums)-1, -1, -1):
            if(i == len(nums)-1):
                postprod[i] = nums[i]
            else:
                postprod[i] = postprod[index]*nums[i]
                index = i
        
        for i in range(0,len(nums)):
            if(i == 0):
                result[i] = postprod[i+1]
            elif(i == (len(nums)-1)):
                result[i] = preprod[i-1]
            else:
                result[i] = postprod[i+1]*preprod[i-1]
        return result
        
