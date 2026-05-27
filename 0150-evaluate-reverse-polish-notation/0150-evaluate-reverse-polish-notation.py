class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operator = ['+', '-', '*', '/']
        for i in tokens:
            if(i in operator):
                b = stack.pop()
                a = stack.pop()
                c = int(eval(f"{a}{i}{b}"))
                stack.append(int(c))
            else:
                stack.append(int(i))
        return int(stack.pop())