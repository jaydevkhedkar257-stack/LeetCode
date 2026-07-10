class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) // 2  # size of left partition

        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi) // 2      # elements taken from nums1 into left half
            j = half - i            # elements taken from nums2 into left half

            left1 = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')
            left2 = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')

            if left1 <= right2 and left2 <= right1:
                # Correct partition found
                if total % 2 == 1:
                    return float(max(left1, left2))
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                hi = i - 1  # took too many from nums1, move left
            else:
                lo = i + 1  # took too few from nums1, move right

        raise ValueError("Input arrays are not sorted properly")