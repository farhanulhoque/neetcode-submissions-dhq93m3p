class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        curMin = min(val, self.stack[-1][1] if self.stack else val)
        self.stack.append((val, curMin))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
    

    # TC: push -> O(1), One append to each stack, one min comparison; pop -> O(1), One pop; top -> O(1), Read [0] of the top tuple; getMin -> O(1), Read [1] of the top tuple
    # SC: O(n) -> Each element stores a pair — still linear, just doubled per entry

    # Solution Description: Instead of two parallel stacks, we use one stack where each entry is a pair: (value, min_so_far). The value is the actual element; min_so_far is the minimum of everything in the stack up to and including this element. Since each entry carries its own min, getMin just reads the top entry's second field — instant. Push and pop operate on single tuples, so the value and its associated min can never fall out of sync.
        
