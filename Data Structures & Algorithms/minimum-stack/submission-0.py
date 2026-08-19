class MinStack:

    def __init__(self):
        self.stack = []
        self.pre_min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        cur_pre_min = self.pre_min[-1] if self.pre_min else float('inf')
        self.pre_min.append(min(val, cur_pre_min))

    def pop(self) -> None:
        self.stack = self.stack[:-1]
        self.pre_min = self.pre_min[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.pre_min[-1]
