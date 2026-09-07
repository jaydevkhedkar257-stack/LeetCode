class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        check_list = []
        def backtrack(i , curr):
            if i >= len(nums):
                if Counter(curr) not in check_list:
                    res.append(curr[:])
                    check_list.append(Counter(curr))
                return
            curr.append(nums[i])
            backtrack(i+1, curr)
            curr.pop()
            backtrack(i+1, curr)
            return
        backtrack(0, [])
        
        return res