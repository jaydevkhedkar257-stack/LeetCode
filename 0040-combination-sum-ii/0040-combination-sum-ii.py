class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        curr = []

        def backtrack(start, total):
            if total == target:
                res.append(curr[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue  # skip duplicates at this level
                if total + candidates[i] > target:
                    break  # sorted, so no point going further
                curr.append(candidates[i])
                backtrack(i + 1, total + candidates[i])
                curr.pop()

        backtrack(0, 0)
        return res