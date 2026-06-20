class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while(l <= r):
            # * (l + r) // 2 can lead to overflow
            # * for large array(not common in py but in other lang)
            mid = l + ((r - l) // 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid+1
            elif nums[mid] > target:
                r = mid-1
        return -1
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix) - 1
        while(i <= j):
            mid1 = (j+i)//2
            if target >= matrix[mid1][0] and target <= matrix[mid1][-1]:
                l = 0
                r = len(matrix[mid1])-1
                while(l <= r):
                    # * (l + r) // 2 can lead to overflow
                    # * for large array(not common in py but in other lang)
                    mid2 = l + ((r - l) // 2)
                    if matrix[mid1][mid2] == target:
                        return True
                    elif matrix[mid1][mid2] < target:
                        l = mid2+1
                    elif matrix[mid1][mid2] > target:
                        r = mid2-1
                return False
            elif target > matrix[mid1][-1]:
                i = mid1 + 1
            elif target < matrix[mid1][0]:
                j = mid1 - 1
        return False
                