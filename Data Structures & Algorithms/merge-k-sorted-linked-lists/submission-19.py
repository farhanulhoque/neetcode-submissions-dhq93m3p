# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Empty input → nothing to merge → return None
        if not lists or len(lists) == 0:
            return None

        # Keep going until only one merged list remains
        while len(lists) > 1:
            # Create a fresh list to collect this round's pairwise merges
            mergedList = []

            # Step through lists two at a time (range(..., 2))
            for i in range(0, len(lists), 2):
                # First list of the pair
                l1 = lists[i]
                # Second list — or None if there's an odd one out at the end
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                # Merge the pair, append the result
                mergedList.append(self.mergeTwo(l1, l2))

            # Replace lists with the (roughly half-sized) merged results
            lists = mergedList
        
        # One list left — that's the fully merged result
        return lists[0]
    
    # Helper — Merge Two Lists
    def mergeTwo(self, l1: ListNode, l2: ListNode):
        # Dummy node + tail pointer to build the merged list
        dummy = ListNode()
        tail = dummy
        
        # Standard two-pointer merge: attach the smaller head each step
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        # Attach whatever remains of the non-empty list
        tail.next = l1 if l1 else l2

        # Return the merged head
        return dummy.next


    # TC: O(n . logk) -> n = total nodes across all lists, k = number of lists. Each round merges all n nodes once (O(n)), and there are log k rounds (halving the list count each time)
    # SC: O(1)  -> We rewire existing nodes in place (dummy + pointers per merge). The mergedList array holds list heads only — O(k) references, not nodes.

    # Solution Description: The naive idea — merge list 1 with list 2, then that result with list 3, then with list 4, and so on — is correct but slow, because early lists get re-traversed over and over. Instead, we merge in pairs: combine lists into k/2 merged lists, then merge those into k/4, and so on until one list remains. This is divide and conquer. Each "round" processes every element once (O(n) total across all pairs), and there are only log k rounds (since we halve the number of lists each time). So instead of k sequential merges, we do log k rounds — a big speedup.


    # -----Deep Dive -----

    # Why pairwise (DIVIDE & CONQUER) merging beats sequential merging -> Sequential: The accumulator grows, and each new merge re-walks everything in it. Early elements get traversed k times → O(k·n) total. Pairwise: Each ROUND touches every element once → O(n) per round, Number of rounds = log k (halving each time) → O(n log k) total. For k = 1000, that's ~10 rounds instead of 1000 passes.

    # Why range(0, len(lists), 2) — stepping by two -> We're merging PAIRS, so we jump two lists at a time. The step of 2 means each iteration grabs a fresh, non-overlapping pair. Stepping by 1 would re-process lists and break the pairing.

    # Why the odd-list-out check if (i + 1) < len(lists) -> If there's an odd number of lists, the last one has no partner. Without the check: lists[i+1] on the last odd element → IndexError. With the check: the lone list merges with None → merge returns it as-is → survives to next round.

    # Why merging with None works cleanly -> In mergeTwo, the while loop is "while l1 AND l2": if l2 is None → loop never runs. So merging any list with None just returns that list.




