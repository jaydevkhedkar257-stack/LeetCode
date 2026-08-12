class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(temp, i, remain):
            if remain == 0:
                res.append(temp[:])
                return
            if remain < 0 or i == len(candidates):
                return
            # include candidates[i], stay at i (reuse allowed)
            temp.append(candidates[i])
            backtrack(temp, i, remain - candidates[i])
            temp.pop()
            # exclude candidates[i]
            backtrack(temp, i + 1, remain)
        backtrack([], 0, target)
        return res