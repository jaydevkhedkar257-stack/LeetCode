class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        start = ["(", "[", "{"]
        end = [")", "]", "}"]
        valid = dict(zip(start, end))
        stack = []
        ptr = -1

        for i in s:
            if ptr == -1 and i not in valid:
                return False

            if i in valid:
                stack.append(valid[i])
                ptr += 1

            elif stack[ptr] == i:
                stack.pop()
                ptr -= 1

            elif stack[ptr] != i:
                return False

        if len(stack) != 0:
            return False

        return True
