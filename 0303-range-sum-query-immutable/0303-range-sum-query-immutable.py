class NumArray:

    def __init__(self, nums: list[int]):
        # Create a prefix sum array with an extra element at index 0 initialized to 0
        self.prefix = [0] * (len(nums) + 1)
        
        # Fill the prefix array
        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        # Calculate sum in O(1) time
        return self.prefix[right + 1] - self.prefix[left]


# Example Usage:
# obj = NumArray([-2, 0, 3, -5, 2, -1])
# print(obj.sumRange(0, 2)) # Output: 1  ((-2) + 0 + 3)
# print(obj.sumRange(2, 5)) # Output: -1 (3 + (-5) + 2 + (-1))
# print(obj.sumRange(0, 5)) # Output: -3