# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Both pointers start at the head
        slow, fast = head, head

        # Continue while fast can take two steps — need both fast and fast.next to exist. If either is None, fast.next.next would crash. 
        while fast and fast.next:
            # slow moves one step forward
            slow = slow.next
            # fast moves two steps forward
            fast = fast.next.next

            # If they're on the same node, fast has met slow → cycle! Return True — cycle confirmed. The "move then check" order is essential because both pointers begin equal. Checking first would give an instant false positive. == on nodes checks object identity (same physical node), which is precisely the cycle condition. Never compare .val for cycle detection — two distinct nodes can share a value.
            if slow == fast:
                return True
        
        # 	fast hit the end (None) → no cycle → return False
        return False

        # TC: O(n) -> No cycle: fast reaches the end in n/2 steps → O(n). With cycle: slow travels at most n steps before fast catches it (fast closes a gap of at most n at 1 node/step) → still O(n)
        # SC: O(1) -> Just two pointers, regardless of list length — this is the big win over the hash set approach

        # Solution Description: Use two pointers that move at different speeds: slow advances one node per step, fast advances two. If the list has no cycle, fast reaches the end (None) and we return false. If there is a cycle, fast eventually laps around and catches up to slow from behind — they land on the same node. Think of two runners on a circular track: the faster one always eventually laps the slower one. When they meet, we've proven a cycle exists.

        # Why do fast and slow ALWAYS meet if there's a cycle? -> fast gains exactly 1 step on slow per iteration. Since the gap changes by exactly 1 each time (never skipping), it's guaranteed to hit exactly 0. If fast gained 2+ per step it could "jump over" slow — but gaining exactly 1 makes a meeting inevitable. fast gains exactly 1 step on slow per iteration. Since the gap changes by exactly 1 each time (never skipping), it's guaranteed to hit exactly 0. If fast gained 2+ per step it could "jump over" slow — but gaining exactly 1 makes a meeting inevitable.
        # Why the loop condition is fast and fast.next -> We check fast (not slow) because fast is the one moving two steps and racing toward the end. slow moves half as fast — it can never hit None before fast does. So guarding fast is sufficient.
        # Why == compares nodes, not values -> In Python, == on two ListNode objects compares IDENTITY (same object) because ListNode doesn't define custom equality. So slow == fast asks: "are these the SAME node in memory?" NOT "do they have the same value?". This is exactly what we want — a cycle means the two pointers land on the literally-same node, not just a node with an equal value. slow and fast might both be ON a node with value 2 — but DIFFERENT nodes. 

