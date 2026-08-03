# Create a Node class. This defines one node in the doubly linked list. Each node is a little box holding four things: two pieces of data (key, val) and two pointers (prev, next). prev and next start as None because a freshly created node isn't linked into the list yet — insert() wires them up.
class Node:
    # Each node stores both its key and val (the key is needed for eviction — explained below). prev and next — doubly linked, so we can traverse both directions
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        # Store the capacity
        self.cap = capacity
        # create a cache hashmap: key → Node for O(1) lookup
        self.cache = {}

        # left dummy — the LRU (least recently used) side
        self.left = Node(0, 0)
        # right dummy — the MRU (most recently used) side
        self.right = Node(0, 0)
        # Wire the two dummies together — an empty list is just left ↔ right
        self.left.next = self.right
        self.right.prev = self.left 
    
    # Helper: remove (Detach the node from the list)
    def remove(self, node):
        # Grab the node's neighbors
        prev, nxt = node.prev, node.next
        # Link the neighbors directly to each other, bypassing the node
        prev.next = nxt
        nxt.prev = prev
    
    # Helper: insert (Insert a node just before right (the MRU position))
    def insert(self, node):
        # The insertion point is between right.prev and right
        prev, nxt = self.right.prev, self.right
        # Wire the node in between them (four pointer updates)
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        # If the key is already cached
        if key in self.cache:
            # Move its node to the front (remove then re-insert = mark as most recent)
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            # Return the value
            return self.cache[key].val
        # Not found → return -1
        return -1      

    def put(self, key: int, value: int) -> None:
        # If the key already exists, remove the old node (we'll re-insert with the new value)
        if key in self.cache:
            self.remove(self.cache[key])
        # Create a fresh node, add to the map, insert at the front
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # If cache exceeds the capacity now
        if len(self.cache) > self.cap:
            # The LRU victim is left.next (the node right after the head dummy)
            lru = self.left.next
            # Remove it from the list and the map
            self.remove(lru)
            del self.cache[lru.key]
    

    # TC: get -> O(1): Map lookup O(1) + remove O(1) + insert O(1)
    #     put -> O(1): Map lookup/insert O(1) + list remove/insert O(1) + eviction O(1)
    # SC: O(Capacity) -> 	The map and list each hold at most capacity nodes (plus 2 sentinels)

    # Every single operation is O(1) because both the lookup (map) and the reordering (doubly linked list) are O(1). Neither structure alone achieves this — the map can't order, the list can't search fast. Their combination is what hits the O(1) requirement.
    
    # Solution Description: We need two things to be O(1): finding a key (lookup) and reordering by recency. No single data structure does both — so we combine two. A hashmap gives O(1) key → node lookup. A doubly linked list maintains usage order: most-recently-used near the head, least-recently-used near the tail. Because it's doubly linked, we can remove any node in O(1) (we have pointers to its neighbors) and the tail node (the LRU victim) is instantly accessible. On get: look up the node, move it to the front (most recent). On put: if the key exists, update and move to front; if new, add to front and — if over capacity — evict the tail. Two dummy sentinel nodes (head and tail) remove all the null-checking edge cases.

    # 





