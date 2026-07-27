# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False

        # TC: O(n) -> 
        # SC: O(1) -> 

        # Solution Description: Use two pointers that move at different speeds: slow advances one node per step, fast advances two. If the list has no cycle, fast reaches the end (None) and we return false. If there is a cycle, fast eventually laps around and catches up to slow from behind — they land on the same node. Think of two runners on a circular track: the faster one always eventually laps the slower one. When they meet, we've proven a cycle exists.
