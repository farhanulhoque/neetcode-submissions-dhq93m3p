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



        # ----- Deep Dive -----

        # Why fast/slow finds the middle (and why fast = head.next) -> 

                # Fast/slow pointers find the middle: fast moves TWICE as fast as slow, so when fast
                # reaches the end, slow is at the middle. (This is the same technique as Linked List
                # Cycle and Find the Duplicate.)

                # The subtlety here is WHERE slow lands, controlled by fast's start:

                #     fast = head.next (one ahead): for an EVEN-length list, slow lands on the END of
                #     the FIRST half (the left-middle). This is what we want — we split AFTER slow, so
                #     the first half gets the extra node (or they're equal).

                #     e.g. [1,2,3,4]: slow ends at 2 (end of first half). split → [1,2] and [3,4].
                #     e.g. [1,2,3,4,5]: slow ends at 3 (the middle). split → [1,2,3] and [4,5].

                #     if fast started at head instead, slow would land one node further, giving the
                #     second half the extra node — which complicates the merge (second half longer than
                #     first). Starting fast = head.next ensures first half ≥ second half, so the merge
                #     (driven by the shorter second half) terminates cleanly.

                # This "fast starts ahead for the left-middle" is the detail that makes the later merge
                # work without extra edge-case handling.
        


        # Why we split the list with slow.next = None -> 

                # Before reversing the second half, we must SPLIT the list into two separate lists:
                #     first half:  head → ... → slow  (ending at slow)
                #     second half: slow.next → ... → end

                # Setting slow.next = None does the cut — it terminates the first half at slow, so the
                # first half is now a complete, independent list ending in None.

                # Why cut? Two reasons:
                #     1. the reverse step needs the second half as its OWN list (with a clear end) to
                #     reverse correctly.
                #     2. without the cut, the first half's tail would still point into the second half,
                #     and after reversing + merging, you'd create a CYCLE or tangle the pointers. 💥

                #     e.g. [1,2,3,4]: slow=2. second = 3→4. slow.next=None → first half is 1→2→None.
                #     now we have two clean lists: [1,2] and [3,4], ready to reverse the second.

                # The cut is a save-before-overwrite discipline: grab `second = slow.next` FIRST (to
                # keep the second half's head), THEN set slow.next = None (to cut). Order matters — if
                # you nulled slow.next first, you'd lose access to the second half.


        # The three-pointer reversal of the second half -> 

                # This reverses the second half using three pointers (the classic reverse). For each
                # node: save the next (tmp), flip the current node's pointer to point backward (prev),
                # then advance both pointers.

                #     [3,4]: 
                #     second=3, prev=None: tmp=4, 3.next=None, prev=3, second=4.
                #     second=4, prev=3:    tmp=None, 4.next=3, prev=4, second=None.
                #     → reversed: 4→3→None. prev=4 is the new head.

                # After the loop, `prev` points to the head of the reversed second half (the ORIGINAL
                # last node, now first). This is what we'll merge from the "back."

                #     why reverse? the reorder interleaves from BOTH ENDS (L0, Ln, L1, Ln-1, ...). By
                #     reversing the second half, the "back" elements (Ln, Ln-1, ...) become a forward
                #     list we can walk normally — so the merge just alternates between the two forward
                #     lists.

                # This is the exact three-pointer reversal from Reverse Linked List — reused as a
                # sub-step here. (Reorder List = fast/slow + reverse + merge, all three core techniques.)


        # The merge — interleaving two halves with careful pointer saves -> 

                # We interleave: take one from the first half, one from the (reversed) second half,
                # alternating. Each iteration splices a second-half node between two first-half nodes.

                # The CRITICAL detail: save BOTH next pointers (tmp1, tmp2) BEFORE rewiring, because
                # rewiring destroys them.

                #     first.next = second → OVERWRITES first's original next (we need it = tmp1).
                #     second.next = tmp1  → OVERWRITES second's original next (we need it = tmp2).

                #     so we grab tmp1 = first.next and tmp2 = second.next FIRST, then rewire, then
                #     advance to tmp1 and tmp2. Classic save-before-overwrite.

                # Walk through [1,2] + [4,3] (first half + reversed second half):
                #     first=1, second=4: tmp1=2, tmp2=3.
                #     1.next=4, 4.next=2 → 1→4→2. advance: first=2, second=3.
                #     first=2, second=3: tmp1=None, tmp2=None.
                #     2.next=3, 3.next=None → ...2→3→None. advance: first=None, second=None.
                #     loop ends (second is None).
                #     result: 1→4→2→3 → the reorder of [1,2,3,4]! ✓ (L0,Ln,L1,Ln-1 = 1,4,2,3)

                # Why loop WHILE second (not first)? Because the second half is ≤ the first half (from
                # the fast=head.next choice in part 1). So second runs out first (or same time) — looping
                # on second ensures we stop cleanly without a null-pointer error. If first were longer,
                # its last node just keeps its existing next (or None) after second is exhausted.








