class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 longer than s2 → no window can fit → early exit
        if len(s1) > len(s2):                        
            return False                             

        # Count characters in s1 — our target frequency map
        s1Count = Counter(s1)    
        # Count the first window of s2 — the first len(s1) characters                    
        window = Counter(s2[:len(s1)])               

        # Initial window already matches → done
        if s1Count == window:                        
            return True                              

        # l marks the left edge of the window
        l = 0 
        # r starts at len(s1) — first character not yet in the window                                        
        for r in range(len(s1), len(s2)):
            # Character entering on the right — increment its count            
            window[s2[r]] += 1                      
            # Character leaving on the left — decrement its count
            window[s2[l]] -= 1 
            # if count hits 0, delete the key entirely                      
            if window[s2[l]] == 0:                   
                del window[s2[l]]   

            # Slide the left edge                
            l += 1                                   

            # Maps are equal → window is a permutation
            if s1Count == window:                    
                return True                          

        return False    
        
        # TC: O(n * m) -> n = len(s2), m = number of distinct characters. Each slide does O(1) count updates but the s1Count == window comparison is O(m)
        # SC: O(m) -> Two maps holding at most m distinct characters

        # Solution Description: Same fixed-size window idea, but uses Counter maps instead of 26-slot arrays so it works for any character set. Count s1 into a target map, build a map for the first window, then slide forward — incrementing the entering character and decrementing the leaving one. The key detail: when a count hits zero, delete the key, since dict equality compares key sets and a leftover {'e': 0} would break the match. Compare the window map to the target after each slide.

        # Even though 'e': 0 means "zero e's in the window" — logically identical to 'e' not being there — Python sees a different key set and reports inequality.
        # Every time a count drops to zero, we remove the key to keep the map clean. This is exactly why the array version never needs this — [0]*26 compares position by position, and a zero in a slot is just... zero. Dicts compare key sets too.

        #  If the interviewer says "what if the string contained unicode?" — that's your cue to reach for the HashMap version. If they say "can you make the comparison O(1)?" — that's the matches counter
        