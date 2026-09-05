class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        max_num = float('-inf')
        min_num = float('inf')
        max_list, min_list = [0]*n, [0]*n
        for i in range(n):
            max_num = max(max_num, nums[i])
            min_num = min(min_num, nums[n-(i+1)])
            max_list[i] = max_num
            min_list[n-(i+1)] = min_num

        for i in range(n):
            if max_list[i] - min_list[i] <= k:
                return i

        return -1