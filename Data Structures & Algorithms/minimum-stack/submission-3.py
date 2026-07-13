class MinStack:

    def __init__(self):
        # Main stack — holds the actual values
        self.stack = []
        # Auxiliary stack — holds the running minimum at each level
        self.minStack = []

    def push(self, val: int) -> None:
        # Add the value to the main stack
        self.stack.append(val)
        # Compute the new min: smaller of val and the current min (or val itself if minStack is empty)
        val = min(val, self.minStack[-1] if self.minStack else val)
        # Push that min onto the min stack
        self.minStack.append(val)

    def pop(self) -> None:
        # Remove from the main stack
        self.stack.pop()
        # Remove from the min stack too — keep them in sync. Each level "remembers" what the min was at that moment, so popping naturally rolls back to the earlier min.
        self.minStack.pop()

    def top(self) -> int:
        # return the main stack's top
        return self.stack[-1]

    def getMin(self) -> int:
        #  return the min stack's top (always the current min)
        return self.minStack[-1]
    

    # TC: push -> O(1), One append to each stack, one min comparison; pop -> O(1), One pop from each stack; top -> O(1), Read the top of the main stack; getMin -> O(1), Read the top of the min stack
    # SC: O(n) -> The min stack doubles the storage — an extra entry per element
    
    # Solution Description: A normal stack can't return its min in O(1) — you'd have to scan all elements. The trick is a second stack (minStack) that stores, at each level, the minimum of everything in the main stack up to that point. When we push a value, we also push min(val, current_min) onto minStack. So minStack's top is always the min of the whole stack. When we pop, we pop from both stacks, keeping them in sync. getMin just reads minStack's top — instant. The key insight: each entry in minStack remembers "what was the minimum when this element was on top," so popping naturally restores the previous minimum.

    # The pattern — "store extra info alongside each element so you never have to recompute" 
    # the "if self.minStack else val" prevents a crash on the very first push, when there's no previous min to compare with.
    # The invariant: len(stack) == len(minStack) ALWAYS. This 1-to-1 correspondence is what makes pop() correct — removing the top of both restores the exact previous state.
    