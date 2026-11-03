class Solution:
    def numDecodings(self, s: str) -> int:
        # Top-down memoization (natural recursion + cache)
        
        # empty suffix = 1 way
        memo = {len(s): 1}                      
        def dfs(i):
            if i in memo: 
                return memo[i]
            # can't start a group with 0
            if s[i] == "0":                     
                memo[i] = 0
                return 0
            # take 1 digit
            ways = dfs(i + 1)                   
            if i + 1 < len(s) and "10" <= s[i:i+2] <= "26":
                # take 2 digits
                ways += dfs(i + 2)              
            memo[i] = ways
            return ways
        return dfs(0)


        # Memoization mirrors the natural “decode from position i” recursion: at each position, take one digit (recurse to i+1) and, if the two-digit group is valid, take two (recurse to i+2), summing the ways. The cache (seeded with “empty suffix = 1 way”) makes each position computed once → O(n). This top-down form is often the easiest to derive — write the recursion, handle the '0' and range checks, add memoization — before converting to the bottom-up/optimized version. A great way to start a DP problem.