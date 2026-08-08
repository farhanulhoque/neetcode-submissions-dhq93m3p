# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Dummy node before head — anchors the result and simplifies the first group's connection
        dummy = ListNode(0, head)
        # This is the node just before the current group (starts at dummy)
        groupPrev = dummy

        # Loop over groups until we run out
        while True:
            # Find the kth node of the current group (the group's last node)
            kth = self.getKth(groupPrev, k)
            # If fewer than k nodes remain → kth is None → stop, leave the rest as-is
            if not kth:
                break
            # This is the first node of the next group (right after this group)
            groupNext = kth.next

            # Set up reversal: prev starts at groupNext (so the group's tail links forward correctly), curr at the group's first node
            prev, curr = kth.next, groupPrev.next
            # Reverse until curr reaches the next group. Standard three-pointer reversal (save, flip, advance)
            while curr != groupNext:
                temp = curr.next
                curr.next = prev 
                prev = curr
                curr = temp
            
            # Reconnect
            # Save the group's old first node (becomes the new tail)
            temp = groupPrev.next
            # Previous group's tail now points to this group's new head (kth)
            groupPrev.next = kth
            # Advance groupPrev to this group's new tail for the next iteration
            groupPrev = temp

        # Return the new head
        return dummy.next

    
    def getKth(self, curr: ListNode, k: int) -> ListNode:
        # Walk forward k steps (or until the list ends)
        while curr and k > 0:
            # Step forward, count down
            curr = curr.next
            k -= 1
        # Return the kth node, or None if the list ended first
        return curr
    

    # TC: O(n) -> Each node is visited a constant number of times: once by getKth (checking the group) and once during reversal. Total work is proportional to n
    # SC: O(1) -> Only a handful of pointers (dummy, groupPrev, prev, curr, tmp, kth) regardless of list length — all reversals are in place

    # Solution Description: We reverse the list in chunks of k. For each group: first, look ahead k nodes to find the group's end (the kth node). If fewer than k nodes remain, we're done — leave them. Otherwise, reverse the k nodes in that group, then carefully reconnect: the previous group's tail must point to this group's new head (the old kth node), and this group's new tail (the old first node) must point to the start of the next group. A dummy node and a groupPrev pointer manage these connections cleanly.


    # ----- Deep Dive -----

    # Why check for k nodes BEFORE reversing (getKth) -> The problem says a final group with fewer than k nodes stays unreversed. So we must verify a full group exists before touching it. getKth walks k steps from groupPrev. If it reaches the kth node → full group exists. If it hits None first → fewer than k nodes remain → getKth returns None → we stop. getKth returning None is the signal that fewer than k nodes remain.

    # Why prev starts at groupNext (not None) -> In standalone reversal, the reversed group's tail should point to None. But here, the reversed group's tail must point to the NEXT GROUP. By starting prev = groupNext, when the reversal finishes, the old first node (now the tail) already points at groupNext.

    # Why the reversal loop condition is while curr != groupNext -> Standard reversal runs while curr (until None). Here we stop at the group boundary, not the list end. We only want to reverse THIS group — k nodes — not the whole list. groupNext marks where this group ENDS (the first node of the next group). So we reverse until curr reaches groupNext, then stop. Using while curr would reverse the entire rest of the list, not just this group.

    # The reconnection dance -> The reconnection does two jobs: (1) point the previous group's tail at this group's new head (kth), and (2) move groupPrev to this group's new tail (the old first node) so the next group connects properly. The tmp save is essential — groupPrev.next changes, so we grab the old value first.

    # Why groupNext = kth.next is saved before reversing -> kth is the LAST node of the current group. kth.next is the FIRST node of the NEXT group. We save it BEFORE reversing because reversal will change kth's next pointer! It marks both the reversal's stopping point and the start of the next group. Save-before-overwrite.

    # Why the dummy node is essential here -> The dummy gives the first group a valid groupPrev (there's nothing before the real head otherwise) and automatically tracks the new head after the first group's reversal. Without a dummy, we'd need special logic to track the new head.





