# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev starts as None — the node before the head is nothing, and this becomes the new tail's next. The None initialization is what makes the old head terminate the reversed list correctly.
        prev = None
        # curr starts at the head — the first node we'll rewire
        curr = head

        # Loop until curr walks off the end (None). Order: save the next node -> reverse the pointer -> move prev forward -> move curr forward
        while curr:
            # Save the next node in a temp variable before we overwrite the pointer — without this we'd lose the rest of the list. The moment we execute curr.next = prev, the ORIGINAL curr.next is gone. If we didn't save it, we'd have no way to reach the rest of the list.
            temp = curr.next
            # Flip curr's pointer to face backward at prev
            curr.next = prev
            # Advance prev to the node we just finished
            prev = curr
            # Advance curr to the saved next node
            curr = temp

        # curr is None, so prev is the old last node — the new head
        return prev

        # TC: O(n) -> We visit each of the n nodes exactly once, doing O(1) pointer work per node
        # SC: O(1) -> Only three pointers (prev, curr, nxt) regardless of list length — we reverse in place, allocating no new nodes
        
        # Solution Description: Walk through the list with two pointers: prev (the node behind us, initially None) and curr (the node we're currently rewiring). For each node, we flip its next pointer to point backward at prev. But before we overwrite curr.next, we must save it — otherwise we lose the rest of the list. After flipping, both pointers step forward. When curr runs off the end, prev is sitting on the old last node, which is now the new head.

        # The discipline: Before you overwrite any pointer, ask "does this pointer let me reach anything I still need?" If yes, save it first. This single habit prevents most linked list bugs.
        # The order encodes a dependency chain: each line uses a value the next line is about to change. Reordering them corrupts that chain. This is worth memorizing as a fixed unit — temp, curr.next, prev, curr in that sequence.
        # prev always trails one step behind curr. When curr reaches None, prev is exactly on the last valid node — which, after reversal, is the new head.

