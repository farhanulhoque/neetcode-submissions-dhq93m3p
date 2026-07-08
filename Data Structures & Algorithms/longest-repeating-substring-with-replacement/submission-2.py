class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countMap = {}
        left = 0
        maxFreq = 0
        longest = 0

        for right in range(len(s)):
            countMap[s[right]] = countMap.get(s[right], 0) + 1
            maxFreq = max(maxFreq, countMap[s[right]])

            while (right - left + 1) - maxFreq > k:
                countMap[s[left]] -= 1
                left += 1
            
            longest = max(longest, right - left + 1)

        return longest        

        # Solution Description: Slide a window across the string, tracking the frequency of each character inside it. The key formula: within any window, the characters we'd need to replace are everyone except the most frequent character. So window_size - count_of_most_frequent gives the replacements needed. If that number exceeds k, the window is invalid — shrink from the left. Otherwise, the window is valid — record its size. We want to make everything match the most frequent character, since that minimizes replacements.

        # max_freq is never decreased, even when we shrink the window and remove characters. max_freq never produces a wrong larger answer — it can only fail to shrink, which is harmless because longest won't grow unless a genuinely better window exists. Recomputing max_freq exactly would be O(26) per shrink and give the same final answer — so we skip it for speed.