class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        for value, ts in reversed(self.store.get(key, [])):
            if ts <= timestamp:
                return value
        return ""
    
    # Scanning from the end, the first qualifying entry is automatically the largest valid timestamp — no candidate tracking needed. But it's O(n) per get.
