# Create a Node class
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left 
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1      

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
    

    # TC:
    # SC: 
    


    # Solution Description: We need two things to be O(1): finding a key (lookup) and reordering by recency. No single data structure does both — so we combine two. A hashmap gives O(1) key → node lookup. A doubly linked list maintains usage order: most-recently-used near the head, least-recently-used near the tail. Because it's doubly linked, we can remove any node in O(1) (we have pointers to its neighbors) and the tail node (the LRU victim) is instantly accessible. On get: look up the node, move it to the front (most recent). On put: if the key exists, update and move to front; if new, add to front and — if over capacity — evict the tail. Two dummy sentinel nodes (head and tail) remove all the null-checking edge cases.

    # 





