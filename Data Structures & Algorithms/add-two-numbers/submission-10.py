# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node — we build the result list after it
        dummy = ListNode()
        # curr tracks the tail of the list we're building
        curr = dummy
        # carry holds any overflow from the previous column (starts at 0)
        carry = 0

        # Continue while either list has digits or there's a leftover carry
        while l1 or l2 or carry:
            # store l1's digit, or 0 if l1 is exhausted
            v1 = l1.val if l1 else 0
            # store l2's digit, or 0 if l2 is exhausted
            v2 = l2.val if  l2 else 0

            # Column sum: both digits plus the incoming carry
            total = v1 + v2 + carry
            # New carry — 1 if total >= 10, else 0
            carry = total // 10
            # The digit to store — the ones place of total
            digit = total % 10
            # Create a new node with that digit, attach it
            curr.next  = ListNode(digit)
            # Advance the builder pointer
            curr = curr.next

            # Advance l1 if it still has nodes
            l1 = l1.next if l1 else None
            # Advance l2 if it still has nodes 
            l2 = l2.next  if l2 else None

        # Return dummy.next — the head of the sum list
        return dummy.next

        # TC: O(n) -> 
        # SC: O(1) -> 

        # Solution Description: Because digits are stored least-significant-first, we can add them in the exact order we encounter them — just like adding numbers by hand from the rightmost column. Walk both lists together. At each step, sum the two current digits plus any carry from the previous step. The result digit is sum % 10, and the new carry is sum // 10. Build the output list node by node using a dummy node. Continue until both lists are exhausted and there's no carry left — a final carry (like 5 + 5 = 10) needs its own extra node.