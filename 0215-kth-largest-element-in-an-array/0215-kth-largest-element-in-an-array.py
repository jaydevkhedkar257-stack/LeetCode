class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)
        
        res = heapq.nlargest(k, nums)

        return res[-1]