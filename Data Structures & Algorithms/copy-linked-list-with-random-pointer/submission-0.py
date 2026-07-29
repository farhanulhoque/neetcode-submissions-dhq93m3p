"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}

        curr = head
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next
        
        return oldToCopy[head]

        

        # Solution Description: The tricky part is the random pointer — it might point to a node later in the list that we haven't cloned yet. So we can't wire pointers as we go in a single naive pass. The fix is a hashmap mapping each original node to its clone, built in two passes. Pass 1: walk the list and create a bare clone (value only) for every node, storing original → clone in the map. Now every clone exists. Pass 2: walk again and, for each original node, look up its clone and set the clone's next and random by looking up the originals' next and random in the map. Because every clone already exists, every lookup succeeds — even forward-pointing random links.