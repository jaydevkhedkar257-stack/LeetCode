class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = []
        i = 0
        j = n
        while i < n or j < 2*n:
            arr.append(nums[i])
            arr.append(nums[j])
            i += 1
            j += 1
        return arr