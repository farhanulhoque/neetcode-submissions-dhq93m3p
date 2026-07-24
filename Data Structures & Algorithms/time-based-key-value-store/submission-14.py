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
        # result is set to default answer "" — returned if no timestamp qualifies
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
    # SC: O(m · n) -> m is the number of distinct keys, n is the total number of values associated with a key — every set call stores one [value, timestamp] pair. Total space = total number of set calls

    # Solution Description: Store each key in a hash map pointing to a list of [value, timestamp] pairs. Because set is called with strictly increasing timestamps, appending keeps each list sorted by timestamp for free — no insertion sort, no re-sorting. For get, we need the value at the largest timestamp ≤ the query. That's a predecessor search: binary search the key's list, and whenever values[mid]'s timestamp qualifies, record it as a candidate and move right to look for an even later (better) one. If it doesn't qualify, move left. When the loop ends, res holds the value from the latest qualifying timestamp — or "" if none ever qualified.
    
    # n in the get complexity is per-key, not global. A key with 3 entries takes ~2 comparisons regardless of how many other keys exist — the hash map isolates each key's timeline.
    # Always check whether "sorted input" is given or must be maintained. Here it's given — and that's what makes set constant time. This problem guarantees set is called with strictly increasing timestamps per key. If that guarantee didn't hold, appending would break sortedness and binary search would be invalid. You'd need bisect.insort — O(n) per set due to element shifting.
    # Why we don't return immediately on a valid hit: Each valid candidate overwrites the previous res, so the last one saved is always the latest qualifying timestamp — exactly what the problem asks for. We want the timestamp that's closest to the input.
    # Why <= in the timestamp comparison -> The spec says timestamp_prev <= timestamp — an exact match is valid. Using strict < would make every query at the exact moment of a set fail — a subtle bug that passes many test cases but breaks on boundary queries.
    # Why res = "" initialized outside the loop -> values = []  →  l=0, r=-1  →  0 <= -1 is False  →  loop never runs  → res stays "". Without the initialization, res would be undefined in both cases(key exists, key  doesn't exist) → NameError. The default is the answer for "nothing qualifies."
    
