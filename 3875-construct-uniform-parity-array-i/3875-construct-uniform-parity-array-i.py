class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        if sum(nums1) % 2 == 0 or len(nums1) == 1:
            return True
        # i, j = 0, len(nums1) - 1
        # while i <= j:
        #     while nums1[i] % 2 == 0:
        #         if nums1[j] % 2 != 0:
        #             nums1[i] = nums1[i] - nums1[j]
        #         j -= 1
        #     j = len(nums1) - 1
        #     i += 1
        return True
