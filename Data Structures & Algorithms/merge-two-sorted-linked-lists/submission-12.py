# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy placeholder node — our real list gets built after it
        dummy = ListNode()
        # tail points at the last node of the list we're building — starts at the dummy
        tail = dummy

        # Loop while both lists still have nodes to compare
        while list1 and list2:
            # Compare the front values — which list has the smaller head? Attach list1's node to the tail of our result then advance list1 to its next node
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            # Otherwise attach list2's node and advance list2
            else:
                tail.next = list2
                list2 = list2.next
            # Move tail to the node we just attached — it's the new end
            tail = tail.next
        
        # If one list is empty, attach the entire remaining other list at once
        tail.next = list1 if list1 else list2

        # Return dummy.next — the real head, skipping the placeholder
        return dummy.next

        # TC: O(n + m) -> n and m are the two list lengths. Each node is visited and attached exactly once
        # SC: O(1) -> We reuse the existing nodes — only a dummy and a tail pointer are created, regardless of list size. No new list is allocated

        # Solution Description: We build one sorted list by repeatedly comparing the front nodes of both lists and attaching the smaller one to our result. To avoid awkward "is this the first node?" logic, we start with a dummy node — a throwaway placeholder that our real list gets built after. A tail pointer always points at the last node we've attached, so we know where to append next. When one list runs out, we attach the entire remaining other list (it's already sorted). Finally we return dummy.next — the real head, skipping the placeholder.

        # Why dummy node? -> The dummy node is a placeholder whose only job is to give tail a valid starting point. We never use its value — we just build after it and return dummy.next at the end. Without dummy: we'd need special logic for the VERY FIRST node, because there's no "tail" to attach to yet.
        # dummy STAYS on the placeholder forever (so we can find the head later). tail MOVES forward as we build (so we always know where to append).
        # Why tail and dummy start as the same node -> dummy is our anchor to find the head at the end; tail is our moving cursor for building. They start together, then tail walks away while dummy stays put.
        # Why "tail.next = list1 if list1 else list2" -> When the loop exits, one list is empty but the other may still have nodes. Since both lists were already sorted, and everything we've placed so far is <= those leftovers, we can attach the ENTIRE remaining list in one shot.



