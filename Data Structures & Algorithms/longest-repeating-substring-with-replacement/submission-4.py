class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Create a frequncy map {character : how many times it appears IN THE CURRENT WINDOW}
        countMap = {}
        left = 0
        maxFreq = 0
        longest = 0

        for right in range(len(s)):
            countMap[s[right]] = countMap.get(s[right], 0) + 1
            maxFreq = max(maxFreq, countMap[s[right]])

            # (right - left + 1) - maxFreq is the number of replacements needed to make the whole window one character. "While the replacements I need exceed my budget k, the window is INVALID"
            while (right - left + 1) - maxFreq > k:
                #  Character at left is leaving the window — decrement its frequency. Shrink the window from the left until it becomes valid again
                countMap[s[left]] -= 1
                # Move the left edge rightward — window is now one smaller
                left += 1
            
            longest = max(longest, right - left + 1)

        return longest  

        # TC: O(n) -> Single pass — right traverses once, left only moves forward. The while shares a budget of n total moves
        # SC: O(1) -> The count dictionary holds at most 26 keys (uppercase letters) — fixed size

        # Solution Description: Slide a window across the string, tracking the frequency of each character inside it. The key formula: within any window, the characters we'd need to replace are everyone except the most frequent character. So window_size - count_of_most_frequent gives the replacements needed. If that number exceeds k, the window is invalid — shrink from the left. Otherwise, the window is valid — record its size. We want to make everything match the most frequent character, since that minimizes replacements.

        # max_freq is never decreased, even when we shrink the window and remove characters. max_freq never produces a wrong larger answer — it can only fail to shrink, which is harmless because longest won't grow unless a genuinely better window exists. Recomputing max_freq exactly would be O(26) per shrink and give the same final answer — so we skip it for speed.
        # (r - l + 1) - max_freq ->  How many characters are NOT the most frequent one. Since we want the entire window to be one distinct character, the cheapest approach is to keep the most frequent character and replace everything else.
        # By shrinking just enough to become valid, we preserve the window's ability to grow again when the right pointer finds more matching characters.
        # We decrement freq in the while loop because the character at l is physically leaving the window — and the count map's only job is to accurately describe what's currently inside. A stale count means a wrong max_freq, which means a wrong validity check, which means a wrong answer.

        # The Universal Sliding Window Rule:
        # Character ENTERS window (r moves right)  →  count[s[r]] += 1
        # Character LEAVES  window (l moves right) →  count[s[l]] -= 1