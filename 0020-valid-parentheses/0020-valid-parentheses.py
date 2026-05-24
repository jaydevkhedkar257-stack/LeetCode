class Solution:
    def isValid(self, s: str) -> bool:
        valid = {"(": ")", "[": "]", "{": "}"}
        stack = []

        for i in s:
            if i in valid:
                stack.append(valid[i])
            elif not stack or stack[-1] != i:
                return False
            else:
                stack.pop()

        return not stack
