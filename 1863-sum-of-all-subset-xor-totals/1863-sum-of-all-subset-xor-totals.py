class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        def backtracking(subset, i):
            nonlocal result
            if i == len(nums):
                xor_val = 0
                for x in subset:
                    xor_val ^= x
                result += xor_val
                return
            subset.append(nums[i])
            backtracking(subset, i+1)
            subset.pop()
            backtracking(subset, i+1)
        backtracking([], 0)
        return result