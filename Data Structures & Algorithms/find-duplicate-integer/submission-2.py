class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # ---- Phase 1: find the meeting point inside the cycle ----
        # Both slow and fast pointers start at index 0
        slow, fast = 0, 0
        # Loop until they meet inside the cycle
        while True:
            # slow follows one pointer (Moves one step)
            slow = nums[slow]
            # fast follows two pointers (Moves two steps)
            fast = nums[nums[fast]]

            # When they meet somewhere inside the cycle, break out of the loop
            if slow == fast:
                break
        
        # ---- Phase 2: find the cycle entrance ----
        # A new pointer starts back at index 0
        slow2 = 0
        # Loop until the two pointers meet (both move one step)
        while True:
            # slow continues from the meeting point, one step at a time
            slow = nums[slow]
            # slow2 moves from the start, one step at a time
            slow2 = nums[slow2]

            # Where they meet is the cycle entrance (the duplicate). slow is the index of the  duplicate element
            if slow == slow2:
                return slow
        
        # TC: O(n) -> Phase 1 meets within O(n) steps (fast closes the cycle gap); phase 2 reaches the entrance in O(n). Total linear.
        # SC: O(1) -> Only a few integer pointers — no hash set, no array modification. This is the whole point.
        
        # Solution Description: The trick: treat each array element as a pointer. From index i, "follow the pointer" to index nums[i]. Because values are in [1, n] and there are n+1 of them, following these pointers always stays in bounds — and the one duplicate value guarantees that two different indices point to the same place, creating a cycle. Finding the duplicate becomes finding the entrance to that cycle — exactly what Floyd's Tortoise and Hare solves. Phase 1: fast/slow pointers until they meet inside the cycle. Phase 2: reset one pointer to the start; move both one step at a time; where they meet is the cycle's entrance, which is the duplicate number.

        # Why the array IS a linked list -> Treat each index as a node, and nums[index] as the "next pointer": from index i → go to index nums[i]. 
        # Why a cycle MUST exist -> Values are in [1, n], and there are n+1 values (indices 0..n). The duplicate value means TWO different indices contain the same number. That number, used as a pointer, is a destination that TWO nodes point to. Two nodes pointing to the same place = the place has two ways in = a cycle.
        # Why we never go out of bounds -> Values are in [1, n], so nums[i] is always a valid index in [1, n]. (Index 0 is the start but no value equals 0, so nothing points back to 0 — index 0 is OUTSIDE the cycle, which matters for phase 2.)
        # Why the duplicate is the cycle ENTRANCE -> The cycle entrance is the node that TWO other nodes point into. those two pointers are two array slots holding the same value. That shared value is the duplicate. So the entrance index equals the duplicate number.
        # Why fast = nums[nums[fast]] -> nums[nums[fast]] is just .next.next translated into array-indexing. The inner nums[fast] is one hop; wrapping it in another nums[...] is the second hop. Same tortoise-and-hare speeds, expressed through array lookups.
        # Why Phase 2 works — the math behind resetting to start -> The distance from the start to the entrance equals the distance from the meeting point to the entrance (modulo full loops). So two pointers, one from the start and one from the meeting point, moving at the same speed, arrive at the entrance simultaneously.
        # Why both pointers start at index 0 -> Starting at index 0 works precisely because 0 is never a value in the array, so index 0 sits before the cycle. Floyd's requires the start to be outside the cycle. If index 0 were inside the cycle, phase 2's math wouldn't line up.



