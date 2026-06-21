import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        
        def hoursNeeded(k):
            return sum(math.ceil(pile / k) for pile in piles)
        
        while lo < hi:
            mid = (lo + hi) // 2
            if hoursNeeded(mid) <= h:
                hi = mid       # mid works, try smaller speed
            else:
                lo = mid + 1   # mid too slow, need bigger speed
        
        return lo