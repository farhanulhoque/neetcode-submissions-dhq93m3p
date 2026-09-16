class Twitter:
    # Solution without using union and nlargest 

    def __init__(self):
        # Global timestamp — increments on every tweet, so tweets are globally orderable
        self.time = 0
        # Map each user to their list of (timestamp, tweetId) tweets
        self.tweets = defaultdict(list)
        # Map each user to a set of who they follow (set → O(1) add/remove)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Post: append (current time, tweetId) to the user's tweet list
        self.tweets[userId].append((self.time, tweetId))
        # Increment the global timestamp so the next tweet is "more recent"
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = []
        for followeeId in self.following[userId]:
            users.append(followeeId)
        users.append(userId)

        minHeap = []
        for u in users:
            for (time, tweetId) in self.tweets[u][-10:]:
                heapq.heappush(minHeap, (time, tweetId))
                
                if len(minHeap) > 10:
                    heapq.heappop(minHeap)
        
        result = []
        while minHeap:
            time, tweetId = heapq.heappop(minHeap)
            result.append(tweetId)
        result.reverse()

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        # Follow: add to the follower's set
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Unfollow: discard (safe even if not present — no error)
        self.following[followerId].discard(followeeId)
    

    # TC: O(F) -> we look at only 10 tweets per user → F users × 10 = 10F tweets pushed → each push/pop O(log 10) = O(1) → O(F) total. F = number of followees (+ self).
    # SC: O(F) -> O(1) for the heap (capped at 10) + O(F) for the users list (dominated by the users list; heap is constant)
    
    # The [-10:] optimization is a one-line change with a real payoff: it bounds getNewsFeed to O(F) regardless of how many tweets each user has posted. It's safe because tweets are time-sorted, so any user's tweets beyond their newest 10 are provably dominated by those 10 — they can never reach a 10-tweet global feed. The slice drops getNewsFeed from O(N) (all tweets) to O(F) (followees × 10).The win: independent of how many tweets each user has (T). A user with 10,000 tweets contributes the same work as one with 10.
    

    # ----- Deep Dive -----

    # Replacing |: just loop the followees into a list and append userId separately. The union was only merging the followee set with the single-element set {userId} — an explicit loop plus one append does the same thing.

    # Replacing nlargest: keep a min-heap capped at size 10, evicting the smallest (oldest) whenever it overflows. This is literally what nlargest does internally — the bounded-heap-of-size-k pattern from Kth Largest. The heap ends up holding the 10 most recent tweets.

    # 

     





        
