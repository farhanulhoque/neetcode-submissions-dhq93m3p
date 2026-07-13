class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
    

    # TC: push -> O(1), One append to each stack, one min comparison; pop -> O(1), One pop from each stack; top -> O(1), Read the top of the main stack; getMin -> O(1), Read the top of the min stack
    # SC: O(n) -> The min stack doubles the storage — an extra entry per element
    
    # Solution Description: A normal stack can't return its min in O(1) — you'd have to scan all elements. The trick is a second stack (minStack) that stores, at each level, the minimum of everything in the main stack up to that point. When we push a value, we also push min(val, current_min) onto minStack. So minStack's top is always the min of the whole stack. When we pop, we pop from both stacks, keeping them in sync. getMin just reads minStack's top — instant. The key insight: each entry in minStack remembers "what was the minimum when this element was on top," so popping naturally restores the previous minimum.

    # The pattern — "store extra info alongside each element so you never have to recompute" 