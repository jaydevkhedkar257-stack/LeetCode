class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        samp = nums.copy()
        heapq.heapify(samp)
        for _ in range(k):
            element = heapq.heappop(samp)
            indx = nums.index(element)
            nums[indx] *= multiplier
            heapq.heappush(samp,nums[indx])
        return nums