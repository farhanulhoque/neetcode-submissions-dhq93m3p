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
                # Second list — or None if there's an odd one out at the end (Bound check)
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

    # Why pairwise (DIVIDE & CONQUER) merging beats sequential merging -> 

            # NAIVE sequential merge: merge list 0 with list 1, then that result with list 2, then
            # with list 3, ... Each merge re-traverses the growing accumulator:
            #     the accumulator grows, and merging the next list re-walks EVERYTHING in it. Early
            #     elements get traversed up to k times → O(Nk) total. Slow.

            # DIVIDE & CONQUER pairwise: merge lists in BALANCED PAIRS, halving the count each round:
            #     round 1: merge (0,1), (2,3), (4,5), ... → k lists become k/2.
            #     round 2: merge those pairs → k/4.
            #     ... → log k rounds until 1 list remains.

            #     each ROUND processes every element ONCE (all pairwise merges in a round total O(N)).
            #     there are log k rounds → O(N log k) total.

            # The saving: no element is re-traversed k times. In each round, every element is touched
            # once, and there are only log k rounds (not k sequential merges).

            #     for k=1000: ~10 rounds vs 1000 sequential passes → 100× fewer passes over the data.

            # This is the SAME divide-and-conquer idea as merge sort — "combine in balanced pairs to
            # get log k rounds instead of k sequential steps."


    
    # Why range(0, len(lists), 2) and the odd-list-out handling -> 

            # STEP BY 2 (range(..., 2)): we process lists in PAIRS, so we jump two at a time:
            #     i=0 → pair (lists[0], lists[1])
            #     i=2 → pair (lists[2], lists[3])
            #     ...
            #     each iteration grabs a fresh, non-overlapping pair. Stepping by 1 would re-process
            #     lists and break the pairing.

            # ODD-LIST-OUT (the i+1 < len check): if there's an ODD number of lists, the last one has
            # no partner:
            #     lists = [L0, L1, L2] (3 lists): i=0 pairs (L0,L1); i=2 → l1=L2, but lists[3] doesn't
            #     exist → l2 = None → mergeTwo(L2, None).
            #     mergeTwo with None just returns the non-None list unchanged (its while loop exits
            #     immediately, and the leftover-attach line grabs L2). So the lone list passes through
            #     to the next round untouched. ✓

            #     without the guard: lists[i+1] on the last odd element → IndexError. 💥

            # So the odd list "just works" — it merges with None (a no-op) and survives to the next
            # round, where it'll pair up as the list count shrinks.


    # Why merging with None works cleanly -> In mergeTwo, the while loop is "while l1 AND l2": if l2 is None → loop never runs. So merging any list with None just returns that list.




