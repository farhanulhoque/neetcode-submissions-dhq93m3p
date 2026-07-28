# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return 
        
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        left, right = 0, len(nodes) - 1
        while left < right:
            nodes[left].next = nodes[right]
            left += 1

            if left == right:
                break
            
            nodes[right].next = nodes[left]
            right -= 1
        
        nodes[left].next = None

        # Dump all nodes into an array (which gives you arr[i] random access that linked lists lack), then use two pointers from both ends to weave them together. The cost is O(n) space for the array of node references.