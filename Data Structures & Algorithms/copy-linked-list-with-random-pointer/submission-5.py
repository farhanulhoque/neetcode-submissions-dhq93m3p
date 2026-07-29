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
        # Map from original node → clone. Pre-seed None → None so null pointers map cleanly. a null pointer in the original maps to a null pointer in the copy, handled by the SAME lookup as every other pointer — no special if-check.
        oldToCopy = {None: None}

        # Start at the head for pass 1 and walk the whole list
        curr = head
        while curr:
            # Create a clone with just the value (pointers set later). In pass 1 we can't set next or random, because the clones they'd point to might not exist yet. So pass 1 does the ONE thing it safely can: copy the value and register the clone in the map.
            copy = Node(curr.val)
            # Record the original → clone mapping
            oldToCopy[curr] = copy
            # Advance to the next original node
            curr = curr.next
        
        # Reset to head for pass 2 and walk the list again
        curr = head
        while curr:
            # Look up this original's clone
            copy = oldToCopy[curr]
            # Set the clone's next to the clone of the original's next
            copy.next = oldToCopy[curr.next]
            # Set the clone's random to the clone of the original's random
            copy.random = oldToCopy[curr.random]
            # Advance to the next original node
            curr = curr.next
        
        # Return the clone of the head
        return oldToCopy[head]

        # TC: O(n) -> Two passes over the list, each O(n). Map lookups and insertions are O(1) average. Total 2n = O(n)
        # SC: O(1) -> The hashmap stores an entry for all n nodes. (The n clones themselves are required output, not counted as extra)

        # Solution Description: The tricky part is the random pointer — it might point to a node later in the list that we haven't cloned yet. So we can't wire pointers as we go in a single naive pass. The fix is a hashmap mapping each original node to its clone, built in two passes. Pass 1: walk the list and create a bare clone (value only) for every node, storing original → clone in the map. Now every clone exists. Pass 2: walk again and, for each original node, look up its clone and set the clone's next and random by looking up the originals' next and random in the map. Because every clone already exists, every lookup succeeds — even forward-pointing random links.

        # Why we need TWO passes -> The random pointer can point forward to a node that doesn't have a clone yet. The two-pass split solves the "forward reference" problem: by the time we wire pointers in pass 2, every clone already exists in the map, so no lookup can fail — regardless of which direction a random pointer faces.
        # Why pre-seed the map with {None: None} -> next and random can be None (end of list, or random points nowhere). When we do:  copy.next = oldToCopy[curr.next], if curr.next is None, we look up oldToCopy[None]. Without the seed: oldToCopy[None] → KeyError! (None was never added as a key). Seeding None → None means null pointers flow through the exact same oldToCopy[...] lookup as real nodes. Without it, you'd need if curr.next else None guards on every pointer assignment. It's the same "eliminate the edge case" philosophy as the dummy node — just applied to a map.
        # Why we look up curr.next and curr.random in the map, not use them directly -> The requirement: the copy must NOT point to any ORIGINAL nodes. If we did copy.next = curr.next: copy would point to the ORIGINAL next node → shared reference → NOT a deep copy. The map translates "original node" → "its clone"
        # Pass 1's job is purely existence — make sure every node has a clone in the map. Pass 2's job is wiring. Separating these two concerns is what makes the forward-reference problem tractable.
