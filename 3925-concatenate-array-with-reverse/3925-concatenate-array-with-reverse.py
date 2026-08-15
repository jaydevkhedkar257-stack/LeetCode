class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        a = nums.copy()
        a.extend(nums[::-1])
        return a