# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedList = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedList.append(self.mergeTwo(l1, l2))

            lists = mergedList
        
        return lists[0]

    def mergeTwo(self, l1: ListNode, l2: ListNode):
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        tail.next = l1 if l1 else l2

        return dummy.next

    # TC: O(n . logk) -> n = total nodes across all lists, k = number of lists. Each round merges all n nodes once (O(n)), and there are log k rounds (halving the list count each time)
    # SC: O(1) -> 	We rewire existing nodes in place (dummy + pointers per merge). The mergedLists array holds list heads only — O(k) references, not nodes.

    # Solution Description: The naive idea — merge list 1 with list 2, then that result with list 3, then with list 4, and so on — is correct but slow, because early lists get re-traversed over and over. Instead, we merge in pairs: combine lists into k/2 merged lists, then merge those into k/4, and so on until one list remains. This is divide and conquer. Each "round" processes every element once (O(n) total across all pairs), and there are only log k rounds (since we halve the number of lists each time). So instead of k sequential merges, we do log k rounds — a big speedup.


    # -----Deep Dive -----

    # 




