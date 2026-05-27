class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operator = ['+', '-', '*', '/']
        for i in tokens:
            if(i in operator):
                b = stack.pop()
                a = stack.pop()
                c = int(eval(f"{a}{i}{b}"))
                stack.append(c)
            else:
                stack.append(i)
        return int(stack[0])