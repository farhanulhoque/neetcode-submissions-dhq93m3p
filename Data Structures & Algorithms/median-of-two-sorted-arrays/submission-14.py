class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Alias the arrays so we can swap them freely
        A, B = nums1, nums2
        # Get total element count across both arrays
        total = len(A) + len(B)
        # half -> how many elements belong in the left partition
        half = total // 2

        # Ensure A is the smaller array — binary searching it is faster and keeps j in range. The swap isn't just an optimization — it's a correctness guard. It also tightens the complexity from O(log(max)) to O(log(min)). If A is the SMALLER array, The most we can take from A is all of it → i goes up to len(A) - 1. Since A is small, i stays small, so j never drops far below -1. j always lands safely inside B.
        if len(B) < len(A):
            A, B = B, A
        
        # Search bounds over A's cut position, not its values
        left, right = 0, len(A) - 1

        # a valid partition is mathematically guaranteed to exist, so we always return from inside
        while True:
            # This is the index of the last element taken from A into the left partition (the mid index / Aleft)
            i = left + (right - left) // 2
            # j is derived, not searched — taking i+1 from A forces j+1 from B. (i + 1 + j + 1 = half -> i + j + 2 = half -> j = half - i -2)
            j = half - i - 2

            # Largest element on A's left side — -∞ if we took nothing from A (out of bound)
            Aleft = A[i] if i >= 0 else float("-inf")
            # Smallest element on A's right side — +∞ if we took all of A (out of bound)
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
            # Largest element on B's left side — -∞ if we took nothing from B (out of bound)
            Bleft = B[j] if j >= 0 else float("-inf")
            # Smallest element on B's right side — +∞ if we took all of B (out of bound)
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")

            # If both cross-comparisons hold → this partition is correct. A valid partition needs every left element ≤ every right element. That sounds like many comparisons — but sortedness gives us most of them for free. Left partition: A[0..i] and B[0..j]. Right partition: A[i+1..] and B[j+1..]. Only the cross-boundary pairs are unverified — two comparisons, O(1). That's why each binary search step stays constant time.
            if Aleft <= Bright and Bleft <= Aright:
                # if Odd total → the right half has one extra element → median is the smallest Aright and Bright
                if total % 2:
                    return min(Aright, Bright)
                # If Even total → average the largest-of-left (Aleft, Bleft) and smallest-of-right (Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            # if A's left is too big → we took too many from A → cut left. A's largest left-side element exceeds B's smallest right-side element
            elif Aleft > Bright:
                right = i - 1
            # Otherwise B's left is too big → we took too few from A → cut right. B's largest left element exceeds A's smallest right element
            else:
                left = i + 1
        
        # TC: O(log(min(m, n))) -> We binary search only over the smaller array's cut positions — min(m,n) candidates, halved each step. Every step does O(1) work: two index computations, four sentinel lookups, two comparisons
        # SC: O(1) -> Only i, j, left, right, and the four boundary values — we never merge or copy the arrays

        # Solution Description: The median splits all m + n elements into a left half and a right half of (nearly) equal size, where every element on the left is ≤ every element on the right. So instead of merging, we search for the correct cut position. If we take i elements from A's front, we're forced to take j = half - i from B to fill the left half — so choosing i determines j. That means we only need to binary search over i. A partition is valid when the two cross-comparisons hold: Aleft ≤ Bright and Bleft ≤ Aright. If Aleft > Bright, we took too much from A → cut further left. If Bleft > Aright, we took too little → cut further right. Once valid, the median reads directly off the four boundary values.

        # Each choice of i produces a DIFFERENT partition of the combined set. We're searching for the i that makes the partition valid. The search space is constructed from the problem's logic, not handed to you. But here the space is positions rather than candidate answers.
        # Why j = half - i - 2 -> We're splitting all the elements into a left partition that holds exactly half elements. Those half elements come partly from A and partly from B. i and j are indices (0-based), but the left partition is measured in element counts. Each array contributes index + 1 elements, so (i+1) + (j+1) = half, which rearranges to j = half - i - 2. The -2 is just correcting for both zero-based indices at once.
        # Why j is derived, not searched -> The left partition size is FIXED at `half`. So the moment you choose i, j is forced → only ONE free variable → binary search over i alone. Choosing i and computing j is what makes this O(log(min(m,n))) instead of quadratic.
        # The ±∞ sentinels (eliminating four edge cases) -> These 4 lines handle the situation where a partition takes everything or nothing from one array. Why -∞ is the right sentinel: Aleft is used in "Aleft <= Bright" — with no elements on A's left, that check should ALWAYS pass. -∞ <= anything. Why +∞ is right: Aright is used in "Bleft <= Aright" — with nothing on A's right, that check should always pass. anything <= +∞. nothing on the LEFT  → -∞  → makes "left <= right" trivially true. nothing on the RIGHT → +∞  → makes "left <= right" trivially true. Without sentinels you'd need four separate if branches for the boundary cases. The ±∞ trick makes them fall through the same two comparisons as every other case.
        # Why the direction logic is Aleft > Bright → go left -> The array whose left side is "too heavy" must give up elements. If A is too heavy, cut A back. If B is too heavy, the only lever is to make A take more — pushing B's forced share down.
        # Why "while True" with no termination check -> A valid partition is MATHEMATICALLY GUARANTEED to exist for any two sorted arrays. There's always exactly one correct cut. So the loop will always hit the return. 
        # Why binary searching the smaller array -> There are two reasons — one about speed, one about correctness. The correctness one is the important one. If A were the LARGER array, i could be large enough that j = half - i - 2  goes very negative — far past -1. The sentinel only handles j == -1 gracefully (as "took nothing from B"). Deeply negative j would silently index B from the wrong end. Searching the smaller array bounds i tightly enough that j always lands in [-1, len(B)-1]. The swap isn't just an optimization — it's a correctness guard. It also tightens the complexity from O(log(max)) to O(log(min)). We search over A's cut positions, and j is derived from i. If A is the larger array, i can get big enough to push j far below -1 — into a range the ±∞ sentinels can't represent correctly, letting invalid partitions slip through. Swapping so A is the smaller array keeps i small, which keeps j inside [-1, len(B)-1] — exactly where the sentinels are valid. The speed boost (log(min) instead of log(max)) is a bonus.

