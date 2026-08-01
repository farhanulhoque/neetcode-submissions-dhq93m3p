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
            # New carry — the TENS digit → the carry to the next column. // 10 extracts the carry to propagate
            carry = total // 10
            # The digit to store — the ones place of total. % 10 extracts the digit to keep
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

        # TC: O(max(m, n)) -> We iterate until the longer list is exhausted (plus possibly one more for a final carry). n and m are the two list lengths. 
        # SC: O(max(m, n)) -> The result list has as many digits as the larger number, plus possibly one extra for a final carry. (Output isn't usually counted, but the new nodes scale with the larger input)

        # Solution Description: Because digits are stored least-significant-first, we can add them in the exact order we encounter them — just like adding numbers by hand from the rightmost column. Walk both lists together. At each step, sum the two current digits plus any carry from the previous step. The result digit is sum % 10, and the new carry is sum // 10. Build the output list node by node using a dummy node. Continue until both lists are exhausted and there's no carry left — a final carry (like 5 + 5 = 10) needs its own extra node.

        # Why "reverse order" storage makes this EASY -> When you add numbers by hand, you start from the RIGHTMOST digit (the ones place) and carry leftward. The lists store digits LEAST-significant first. Walking the lists front-to-back gives us: ones first, then tens, then hundreds = EXACTLY the order we add by hand. The carry flows in the SAME direction we're walking. If digits were stored MOST-significant first (normal order): We'd have to add from the BACK of the list forward. We'd need to reverse both lists first.
        # Why while l1 or l2 or carry — all three conditions -> l1: keep going while list 1 has digits, l2: keep going while list 2 has digits (OR, not AND — the lists can be DIFFERENT lengths), carry: keep going if there's a leftover carry, EVEN when both lists are exhausted! With "l1 OR l2", we continue until BOTH are done. The classic bug is forgetting carry and dropping the leading 1 on sums like 5 + 5.
        # Why "v1 = l1.val if l1 else 0" — the null guard -> When the lists are different lengths, one runs out before the other. Once l1 is None, it contributes 0 to every remaining column.
        # The carry math — // 10 and % 10 -> total // 10 → the TENS digit → the carry to the next column. total % 10 → the ONES digit → what we store in this node. Why carry is always 0 or 1: max total = 19 → 19 // 10 = 1, so carry can NEVER exceed 1



