# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if  l2 else 0

            total = v1 + v2 + carry
            carry = total // 10
            digit = total % 10

            curr.next  = ListNode(digit)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next  if l2 else None

        return dummy.next

        # Solution Description: Because digits are stored least-significant-first, we can add them in the exact order we encounter them — just like adding numbers by hand from the rightmost column. Walk both lists together. At each step, sum the two current digits plus any carry from the previous step. The result digit is sum % 10, and the new carry is sum // 10. Build the output list node by node using a dummy node. Continue until both lists are exhausted and there's no carry left — a final carry (like 5 + 5 = 10) needs its own extra node.