class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t.isdigit() or t[0] == '-' and t[1:].isdigit():
                stack.append(t)
            elif t == '+':
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif t == '-':
                op_2, op_1 = int(stack.pop()), int(stack.pop())
                stack.append(op_1 - op_2)
            elif t == '*':
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif t == '/':
                op_2, op_1 = int(stack.pop()), int(stack.pop())
                stack.append(op_1 / op_2)
        return int(stack[-1])