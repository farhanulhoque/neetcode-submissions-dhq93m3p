# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # ---- Phase 1: find the middle (fast/slow) ----
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # ---- Phase 2: reverse the second half ----
        second = slow.next
        slow.next = None
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # ---- Phase 3: merge the two halves ----
        first, second = head, prev
        while second:
             temp1, temp2 = first.next, second.next
             first.next = second
             second.next = temp1
             first = temp1
             second = temp2
        
        # TC: O(n) -> Three sequential phases, each O(n): find middle (n/2), reverse (n/2), merge (n/2). Total 3 · n/2 = O(n)
        # SC: O(1) -> All three phases rewire existing nodes in place — only a handful of pointers, no new list or array
        
        # Solution Description: The target order [0, n-1, 1, n-2, ...] is exactly what you get by interleaving the first half of the list with the reversed second half. So the solution has three phases: 1. Find the middle using fast/slow pointers — slow lands at the midpoint when fast reaches the end, 2. Reverse the second half using the three-pointer technique, 3. Merge the two halves, alternating one node from each.


