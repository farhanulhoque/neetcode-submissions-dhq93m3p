# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # Create the min-heap that will hold the current front node of each list
        heap = []
        # Loop over each list, with i as its index and node as its head
        for i, node in enumerate(lists):
            # Only seed non-empty lists (skip any list whose head is None). Push the head as a tuple (value, list-index, node) — value orders the heap, i is the tiebreaker, node is the actual node
            if node:
                heapq.heappush(heap, (node.val, i, node))   # (value, tiebreaker, node)

        # Dummy node placed before the real head, so building the merged list needs no first-node special case
        dummy = ListNode()
        # tail tracks the end of the merged list being built; starts at the dummy
        tail = dummy

        # Keep merging while the heap has nodes (i.e. while any list still has unconsumed nodes)
        while heap:
            # Pop the smallest front node across all lists (the global minimum) — unpack its value, list-index, and node
            val, i, node = heapq.heappop(heap)   
            # Append that node to the merged list (link it after the current tail)
            tail.next = node
            # Advance the tail to the newly appended node
            tail = tail.next
            # If the popped node's list has a next node
            if node.next:      
                # push that next node into the heap (restock the heap from the list the min came from)
                heapq.heappush(heap, (node.next.val, i, node.next))
                
        # Return the real head of the merged list (dummy.next)
        return dummy.next



        # Keeps a min-heap of the current head of each list. Repeatedly pop the smallest and push its successor. Same O(n log k) time — the heap has at most k elements, so each push/pop is O(log k), done n times. The i tiebreaker prevents comparing ListNode objects when values tie (Python can't compare nodes). Uses O(k) space for the heap. Both approaches are excellent interview answers — divide & conquer is O(1) space, the heap is arguably more intuitive ("always take the global minimum"). Know both; mention the space tradeoff.


        # ----- Deep Dive -----

        # 






        