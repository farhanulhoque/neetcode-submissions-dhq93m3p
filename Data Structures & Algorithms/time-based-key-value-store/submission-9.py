class TimeMap:

    def __init__(self):
        # Initialize a hashmap: each key maps to a list of [value, timestamp] pairs in chronological order
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # First time seeing this key → initialize an empty list
        if key not in self.store:
            self.store[key] = []
        # Append the new entry. Since timestamps increase, the list stays sorted automatically
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # result is set default answer "" — returned if no timestamp qualifies
        result = ""
        # Fetch this key's list; .get(key, []) safely returns empty [] if key is unknown
        values = self.store.get(key, [])

        # Set binary search bounds over the values list
        left, right = 0, len(values) - 1
        while left <= right:
            # Find Overflow-safe midpoint
            mid = left + (right - left) // 2

            # Does this entry's timestamp qualify (≤ the query)? If Yes — it's a valid candidate, save its value
            if values[mid][1] <= timestamp:
                result = values[mid][0]
                # a later timestamp might also qualify → search right for a better one
                left = mid + 1
            # Timestamp (values[mid][1]) too large — this entry is in the future → search left
            else:
                right = mid - 1
        # Return the best candidate found, or "" if none
        return result
    
    # TC: set -> O(1), Dictionary lookup O(1) + list append O(1) amortized. No sorting — timestamps arrive in order
    #     get -> O(log n), Binary search over that key's list, where n = entries for that key (not total entries). Each step is O(1)
    # SC: O(m · n) -> m distinct keys, n entries each — every set call stores one [value, timestamp] pair. Total space = total number of set calls

    # Solution Description: Store each key in a hash map pointing to a list of [value, timestamp] pairs. Because set is called with strictly increasing timestamps, appending keeps each list sorted by timestamp for free — no insertion sort, no re-sorting. For get, we need the value at the largest timestamp ≤ the query. That's a predecessor search: binary search the key's list, and whenever values[mid]'s timestamp qualifies, record it as a candidate and move right to look for an even later (better) one. If it doesn't qualify, move left. When the loop ends, res holds the value from the latest qualifying timestamp — or "" if none ever qualified.
    
    # n in the get complexity is per-key, not global. A key with 3 entries takes ~2 comparisons regardless of how many other keys exist — the hash map isolates each key's timeline.
    # 

