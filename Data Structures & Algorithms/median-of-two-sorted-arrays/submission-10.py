class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Alias the arrays so we can swap them freely
        A, B = nums1, nums2
        # Get total element count across both arrays
        total = len(A) + len(B)
        # half -> how many elements belong in the left partition
        half = total // 2

        # Ensure A is the smaller array — binary searching it is faster and keeps j in range
        if len(B) < len(A):
            A, B = B, A
        
        # Search bounds over A's cut position, not its values
        left, right = 0, len(A) - 1

        # a valid partition is mathematically guaranteed to exist, so we always return from inside
        while True:
            # This is index of the last element taken from A into the left partition (the mid index)
            i = left + (right - left) // 2
            # j is derived, not searched — taking i+1 from A forces j+1 from B
            j = half - i - 2

            # Largest element on A's left side — -∞ if we took nothing from A (out of bound)
            Aleft = A[i] if i >= 0 else float("-inf")
            # Smallest element on A's right side — +∞ if we took all of A (out of bound)
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
            # Largest element on B's left side — -∞ if we took nothing from B (out of bound)
            Bleft = B[j] if j >= 0 else float("-inf")
            # Smallest element on B's right side — +∞ if we took all of B (out of bound)
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")

            # If both cross-comparisons hold → this partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # if Odd total → the right half has one extra element → median is its smallest
                if total % 2:
                    return min(Aright, Bright)
                # If Even total → average the largest-of-left and smallest-of-right
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            # if A's left is too big → we took too many from A → cut left
            elif Aleft > Bright:
                right = i - 1
            # Otherwise B's left is too big → we took too few from A → cut right
            else:
                left = i + 1
        
        # TC: O(log(min(m, n))) -> We binary search only over the smaller array's cut positions — min(m,n) candidates, halved each step. Every step does O(1) work: two index computations, four sentinel lookups, two comparisons
        # SC: O(1) -> Only i, j, l, r, and the four boundary values — we never merge or copy the arrays

        # Solution Description: The median splits all m + n elements into a left half and a right half of (nearly) equal size, where every element on the left is ≤ every element on the right. So instead of merging, we search for the correct cut position. If we take i elements from A's front, we're forced to take j = half - i from B to fill the left half — so choosing i determines j. That means we only need to binary search over i. A partition is valid when the two cross-comparisons hold: Aleft ≤ Bright and Bleft ≤ Aright. If Aleft > Bright, we took too much from A → cut further left. If Bleft > Aright, we took too little → cut further right. Once valid, the median reads directly off the four boundary values.

        # Each choice of i produces a DIFFERENT partition of the combined set. We're searching for the i that makes the partition valid. The search space is constructed from the problem's logic, not handed to you. But here the space is positions rather than candidate answers.
        # Why j = half - i - 2 -> 
        # Why j is derived, not searched -> 


