# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Dummy node placed before the head (ListNode(0, head) sets its next to head) — makes head-removal uniform
        dummy = ListNode(0, head)
        # left starts at the dummy — it will end up before the target node
        left = dummy
        # right starts at the actual head
        right = head

        # Advance right by n steps to create the gap
        while n > 0:
            # Move right forward, counting down n
            right = right.next
            n -= 1
        
        # Now move both pointers until right falls off the end
        while right:
            left = left.next
            right = right.next
        
        # left is right before the target — splice the target out by skipping over it. Removal in a linked list is just rerouting the previous node's pointer to skip the target. The bypassed node becomes unreachable and is cleaned up automatically. No shifting, no re-indexing — one pointer change.
        left.next = left.next.next

        # Return dummy.next — the head (which may have changed if we removed the original head)
        return dummy.next

        # TC: O(n) -> Where n here is the list length (not the parameter). right traverses the whole list once — the two phases together are a single pass
        # SC: O(1) -> 	Just a dummy node and two pointers, regardless of list length

        # Solution Description: To remove the nth node from the end in a single pass, we use two pointers separated by a fixed gap of n nodes. First, advance right by n steps so it's n ahead of left. Then move both pointers together until right reaches the end. At that moment, the gap guarantees left is sitting exactly on the node just before the one we want to remove — so we splice it out with left.next = left.next.next. A dummy node before the head lets us handle the "remove the first node" case without special logic.

        # Why the gap of n lands left in exactly the right spot -> Set up a gap of n between right and left, then move both together. The gap NEVER changes. So when right hits the end (None), left is always exactly n nodes behind the end. "n nodes behind the end" for LEFT means left is at the node just BEFORE the nth-from-end node.
        # Why the dummy node is ESSENTIAL here -> Without the dummy, removing the first node has no "previous node" to rewire — you'd need a separate if branch. The dummy provides a phantom predecessor for the head, so the same left.next = left.next.next line works whether or not the head is the target.
        # Why left starts at dummy but right starts at head -> Starting left at the dummy (one behind right at head) is what makes left stop before the target rather than on it. That one-node head start is essential for the splice to work. If both started at head, left would end up ON the target itself, and we couldn't rewire the previous node's pointer.



