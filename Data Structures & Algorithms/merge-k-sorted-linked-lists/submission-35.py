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

        # Why a min-heap of the k list heads gives the global minimum ->

                # To merge k sorted lists, at each step you want the SMALLEST value among the current
                # heads of all k lists — that's the next node in the merged output.

                # A min-heap of the k heads gives exactly this: heappop returns the smallest head in
                # O(log k). After taking a node, we push that list's NEXT node (its new head) into the
                # heap, so the heap always holds "the current front of each list."

                #     heap holds AT MOST k nodes at a time (one per list). Each pop gives the global min;
                #     each push restocks from the list the min came from.

                #     lists: [1→4→5], [1→3→4], [2→6]
                #     heap seeded with heads: {1, 1, 2}. pop 1 (from list 0) → output 1, push 4 (list 0's
                #     next). heap now {1, 4, 2}. pop 1 (list 1) → output, push 3. ... always the global
                #     smallest emerges.

                # Why not just compare all k heads directly each step? That's O(k) per node → O(Nk)
                # total. The heap makes "find the min of k" O(log k) → O(N log k) total. The heap is the
                # efficient "repeatedly grab the global minimum from k sources" tool.



        # Why the tuple includes i (the tiebreaker) — the node-comparison trap -> 

                # We push tuples (val, i, node). The heap compares tuples ELEMENT BY ELEMENT: first by
                # val. But what if two nodes have the SAME val? Then the heap compares the NEXT tuple
                # element.

                # WITHOUT the i: the tuple would be (val, node). On a val tie, the heap tries to compare
                # the NODES themselves (node < node) — but ListNode objects aren't comparable → Python
                # throws a TypeError. 

                # WITH the i (a unique list index): on a val tie, the heap compares the i's (integers,
                # always comparable) → breaks the tie cleanly, never reaching the node comparison.

                #     two nodes both with val=1: tuples (1, 0, nodeA) vs (1, 1, nodeB). Heap compares
                #     val (tie: 1==1), then i (0 < 1) → resolved. The nodes are never compared. ✓

                # The i serves as a GUARANTEED-UNIQUE, COMPARABLE tiebreaker. Any unique comparable value
                # works (a counter, an id); the list index i is convenient (always distinct per list).
                # This is a classic "heap of objects" gotcha — you need a comparable tiebreaker before
                # the non-comparable object in the tuple.



        # Why the dummy node simplifies building the merged list -> 

                # We build the merged list by appending nodes to a growing tail. The DUMMY node is a
                # placeholder BEFORE the real head, so we never special-case "is this the first node?"

                #     without dummy: the first node appended would need special handling to set the head,
                #     then subsequent nodes append to the tail — two code paths.
                #     with dummy: every node (including the first) is just tail.next = node; tail = tail.next
                #     — ONE uniform path. The real head is dummy.next (what we return).

                #     dummy → [first] → [second] → ... → tail
                #     return dummy.next = the first real node.

                # This is the "use a dummy when BUILDING a new list" pattern (from Merge Two Lists, Add
                # Two Numbers, etc.) — it eliminates the empty-list / first-node edge case. The tail
                # pointer tracks where to append next.






        