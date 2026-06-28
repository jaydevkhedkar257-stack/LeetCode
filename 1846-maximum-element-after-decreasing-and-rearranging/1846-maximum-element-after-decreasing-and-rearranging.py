class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        if len(arr) == 1: return 1
        sList = sorted(arr)
        sList[0] = 1
        max_num = 1
        for i in range(1,len(sList)):
            if abs(sList[i] - sList[i - 1]) > 1:
                sList[i] = sList[i - 1]+1
            max_num = max(max_num,sList[i])
        return max_num