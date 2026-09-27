class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        target = [(2 * (x % k)) % k for x in nums]
        ans = 0
        for l in range(n):
            s = 0
            cnt = {}
            for r in range(l, n):
                s += nums[r]
                t = target[r]
                cnt[t] = cnt.get(t, 0) + 1
                if s % k == 0 or cnt.get(s % k, 0) > 0:
                    ans = max(ans, r - l + 1)
        return ans