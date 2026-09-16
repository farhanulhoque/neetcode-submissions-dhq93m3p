class Twitter:
    # merge-k-with-pointers approach

    def __init__(self):
        # Global counter that decreases with each tweet — newer tweets get more negative values (the max-heap-by-recency trick)
        self.count = 0
        # Map each user to their list of (timestamp, tweetId) tweets
        self.tweets = defaultdict(list)
        # Map each user to a set of who they follow (set → O(1) add/remove)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Post: append (current time, tweetId) to the user's tweet list
        self.tweets[userId].append((self.count, tweetId))
        # Decrement the global count so the next tweet is "more recent" (more negative)
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # The result list of tweet IDs to return
        result = []
        # Min-heap for merging tweets across users
        minHeap = []

        # Add the user to their own follow set so their own tweets appear in the feed
        self.following[userId].add(userId)
        # Loop over everyone the user follows (plus themself)
        for followeeId in self.following[userId]:
            # Only consider users who have actually posted (exist in tweetMap)
            if followeeId in self.tweets:
                # index = position of that user's newest tweet (last in their list)
                index = len(self.tweets[followeeId]) - 1
                # Grab that newest tweet's count and tweetId
                count, tweetId = self.tweets[followeeId][index]
                # Push [count, tweetId, followeeId, index - 1] — the tweet plus a pointer (index - 1) to that user's next-older tweet
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        
        # Pop until the heap is empty or we have 10 tweets
        while minHeap and len(result) < 10:
            # Pop the globally newest tweet (smallest count = most negative = most recent)
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            # Add its ID to the result
            result.append(tweetId)
            # If that user has an older tweet (index >= 0), we can pull it in next
            if index >= 0:
                # Fetch that user's next-older tweet at index
                count, tweetId = self.tweets[followeeId][index]
                # Push it with an updated pointer (index - 1) — advancing only this user's pointer
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        
        # Return the up-to-10 most recent tweet IDs
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        # Follow: add to the follower's set
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Unfollow: discard (safe even if not present — no error)
        self.following[followerId].discard(followeeId)
    


    # ----- Deep Dive -----

    # The decreasing counter -> The counter decreases so newer tweets get more negative values — and since a min-heap pops the smallest first, it naturally yields newest-first. This is a slick way to get max-heap-by-recency from a min-heap without negating at read time; the "negation" is baked into counting down.

    # getNewsFeed is Merge k Sorted Lists with pointers -> each user's tweets form a recency-sorted list, and the heap holds one tweet per user (a pointer). Pop the globally newest, advance only that user's pointer, repeat 10 times. The heap stays O(F) and stops early — the optimal top-10 merge.

    # The 4-tuple [count, tweetId, followeeId, index - 1] — why each field -> count: the sort key (heap orders by this — recency), tweetId: what we actually output to the feed, followeeId: WHICH user this tweet belongs to (needed to find their next tweet), index - 1: a POINTER to that user's next-older tweet. The last two are the "pointer" machinery: when we pop this tweet, we use followeeId + index to fetch that same user's next-older tweet and push it. Without followeeId, we couldn't know whose list to advance. Without index, we couldn't know WHERE in their list to continue.

    # Why index - 1 and the index >= 0 guard -> When we push a tweet, we store index - 1 = the position of that user's NEXT-older tweet (one step back in their chronological list [oldest....newest]). The guard "if index >= 0" checks whether that user still has an older tweet. Without the guard, index = -1 would wrongly fetch tweetMap[followeeId][-1] (Python's last element!) → an already-seen tweet → duplicates / wrong feed.

    # Why len(res) < 10 and early termination -> we stop after 10 pops no matter how many tweets exist. Combined with the pointer approach (one entry per user), this means we never process more tweets than needed. The minHeap condition handles the case where fewer than 10 tweets exist total.

    # The self-follow line and its subtlety -> Adding userId to their own follow set includes their own tweets in the feed — but it does so by permanently mutating state inside a read method, so the user "follows themselves" after the first feed fetch. Harmless here (you always want your own tweets), but a temporary union (self.followMap[userId] | {userId}) would achieve the same without the side effect.









