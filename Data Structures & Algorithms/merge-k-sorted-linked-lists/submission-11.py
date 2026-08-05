# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        # seed the heap with the head of each list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))   # (value, tiebreaker, node)

        dummy = ListNode()
        tail = dummy
        while heap:
            val, i, node = heapq.heappop(heap)    # smallest current value across all lists
            tail.next = node
            tail = tail.next
            if node.next:                          # push the next node from that same list
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next



        # Keeps a min-heap of the current head of each list. Repeatedly pop the smallest and push its successor. Same O(n log k) time — the heap has at most k elements, so each push/pop is O(log k), done n times. The i tiebreaker prevents comparing ListNode objects when values tie (Python can't compare nodes). Uses O(k) space for the heap. Both approaches are excellent interview answers — divide & conquer is O(1) space, the heap is arguably more intuitive ("always take the global minimum"). Know both; mention the space tradeoff.