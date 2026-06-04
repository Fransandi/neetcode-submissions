class MinStack:

    def __init__(self):
        self.min_stack = []
        self.stack = []
        
    def push(self, val: int) -> None:
        min_val = min(val, self.getMin()) if self.min_stack else val
        
        self.stack.append(val)
        self.min_stack.append(min_val)

    def pop(self) -> None:
        del self.stack[-1]
        del self.min_stack[-1]
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
