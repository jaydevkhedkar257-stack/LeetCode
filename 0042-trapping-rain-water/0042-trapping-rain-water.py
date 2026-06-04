class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_l = max_r = area = 0

        while l < r:
            if height[l] <= height[r]:
                if height[l] >= max_l:
                    max_l = height[l]
                else:
                    area += max_l - height[l]
                l += 1
            else:
                if height[r] >= max_r:
                    max_r = height[r]
                else:
                    area += max_r - height[r]
                r -= 1

        return area