class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A
        
        left, right = 0, len(A) - 1

        while True:
            i = left + (right - left) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                right = i - 1
            else:
                left = i + 1

        # Solution Description: The median splits all m + n elements into a left half and a right half of (nearly) equal size, where every element on the left is ≤ every element on the right. So instead of merging, we search for the correct cut position. If we take i elements from A's front, we're forced to take j = half - i from B to fill the left half — so choosing i determines j. That means we only need to binary search over i. A partition is valid when the two cross-comparisons hold: Aleft ≤ Bright and Bleft ≤ Aright. If Aleft > Bright, we took too much from A → cut further left. If Bleft > Aright, we took too little → cut further right. Once valid, the median reads directly off the four boundary values.

