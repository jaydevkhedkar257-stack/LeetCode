class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        for i in operations:
            if "+" in set(i):
                X += 1
            else:
                X -= 1
        return X