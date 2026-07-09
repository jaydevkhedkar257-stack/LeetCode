class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        j = 0
        i = m
        while(i < n+m):
            nums1[i] = nums2[j]
            i += 1
            j += 1
        nums1.sort()