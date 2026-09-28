class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start + (2 * i) for i in range(n)]
        xor_sum = nums[0]
        for i in nums[1:]:
            xor_sum ^= i
        return xor_sum