"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # The O(1) space interweaving trick
        
        # Pass 1: insert each clone RIGHT AFTER its original
        curr = head
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy          # original → clone → original.next
            curr = copy.next

        # Pass 2: wire random pointers using the interleaving
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next   # clone's random = original.random's clone
            curr = curr.next.next

        # Pass 3: separate the two interleaved lists
        dummy = Node(0)
        copyTail = dummy
        curr = head
        while curr:
            copyTail.next = curr.next     # extract the clone
            copyTail = copyTail.next
            curr.next = curr.next.next    # restore the original
            curr = curr.next
        return dummy.next

        # This version avoids the hashmap by weaving clones directly into the original list (1 → c1 → 2 → c2 → 3 → c3). Then curr.next.random = curr.random.next sets each clone's random using the interleaving — a clone always sits right after its original, so original.random.next is the clone of the random target. Finally it un-weaves the two lists. It's O(1) space but genuinely tricky — three passes of careful pointer surgery.

