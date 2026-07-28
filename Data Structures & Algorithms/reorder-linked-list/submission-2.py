# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # ---- Phase 1: find the middle (fast/slow) ----
        # slow at head, fast one ahead at head.next — this offset makes slow stop at the end of the first half for both odd and even lengths
        slow, fast = head, head.next
        # Standard fast/slow loop condition. slow moves one, fast moves two — when fast finishes, slow is at the midpoint
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # ---- Phase 2: reverse the second half ----
        # second = the start of the second half (node after slow)
        second = slow.next
        # Cut the list in two — the first half now ends at slow. Without the cut, the first half still points into the second half, and after reversing we'd have a tangled mess (possibly a cycle).
        slow.next = None
        # prev starts as None (the reversal's new tail terminator)
        prev = None
        # The three-pointer reversal — reverses the second half in place
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # ---- Phase 3: merge the two halves ----
        # first = head of first half; second = prev = head of the reversed second half
        first, second = head, prev
        # Loop while the second half still has nodes. After splitting, the second half is ALWAYS <= the first half in length. So `second` runs out FIRST (or at the same time). Checking only `second` is sufficient — when it's empty, we're done. The first half might have one leftover node (the middle on odd lengths), which is already correctly pointed to by the previous merge step.
        while second:
            # Save both next-pointers before rewiring. We're about to overwrite first.next AND second.next. Both original values are needed to continue → save both first.
             temp1, temp2 = first.next, second.next
            # Point first's node at second's node
             first.next = second
            # Point second's node at the saved next of the first half
             second.next = temp1
            # Advance both first and second pointers using the saved references
             first = temp1
             second = temp2
        
        # TC: O(n) -> Three sequential phases, each O(n): find middle (n/2), reverse (n/2), merge (n/2). Total 3 · n/2 = O(n)
        # SC: O(1) -> All three phases rewire existing nodes in place — only a handful of pointers, no new list or array
        
        # Solution Description: The target order [0, n-1, 1, n-2, ...] is exactly what you get by interleaving the first half of the list with the reversed second half. So the solution has three phases: 1. Find the middle using fast/slow pointers — slow lands at the midpoint when fast reaches the end, 2. Reverse the second half using the three-pointer technique, 3. Merge the two halves, alternating one node from each.

        # Starting fast at head.next makes the first half take the extra node on odd-length lists. That matches the target pattern [0, n-1, 1, ...] which starts and can end with first-half nodes. If we started fast = head, the split would land differently and the merge would misalign.
        # Because the second half is never longer than the first, while second is the correct guard. The first half's possible extra node (the odd-length middle) naturally ends up as the final node.


