class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):                        
            return False                             

        s1Count = Counter(s1)                        
        window = Counter(s2[:len(s1)])               

        if s1Count == window:                        
            return True                              

        l = 0                                        
        for r in range(len(s1), len(s2)):            
            window[s2[r]] += 1                      

            window[s2[l]] -= 1                       
            if window[s2[l]] == 0:                   
                del window[s2[l]]                    
            l += 1                                   

            if s1Count == window:                    
                return True                          

        return False                                 

        # Solution Description: Same fixed-size window idea, but uses Counter maps instead of 26-slot arrays so it works for any character set. Count s1 into a target map, build a map for the first window, then slide forward — incrementing the entering character and decrementing the leaving one. The key detail: when a count hits zero, delete the key, since dict equality compares key sets and a leftover {'e': 0} would break the match. Compare the window map to the target after each slide.