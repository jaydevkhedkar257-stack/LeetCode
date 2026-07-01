from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_nums = []
        q = deque() # Stores indices of elements
        
        for i in range(len(nums)):
            # 1. Remove indices that are out of the current window bounds
            if q and q[0] < i - k + 1:
                q.popleft()
                
            # 2. Remove smaller elements from the back (they can't be the max)
            while q and nums[q[-1]] < nums[i]:
                q.pop()
                
            # 3. Add the current element's index
            q.append(i)
            
            # 4. Once our window reaches size k, the front of the queue is the max
            if i >= k - 1:
                max_nums.append(nums[q[0]])
                
        return max_nums