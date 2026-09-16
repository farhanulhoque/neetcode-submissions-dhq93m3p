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
        # list of the users whose tweets belong in the feed (including the user themself)
        users = []
        # Add everyone this user follows
        for followeeId in self.following[userId]:
            users.append(followeeId)
        # Add the user themself (feed includes their own tweets)
        users.append(userId)

        # The min-heap, which we'll cap at size 10
        minHeap = []
        # Loop over each relevant user
        for u in users:
            # Take only that user's last 10 tweets — older ones can't reach the top 10
            for (time, tweetId) in self.tweets[u][-10:]:
                # Push (time, tweetId) — no negation, since we want a min-heap to evict olds
                heapq.heappush(minHeap, (time, tweetId))
                
                # If the heap exceeds 10, pop the smallest (oldest) — it can't be in the 10 most recent
                if len(minHeap) > 10:
                    heapq.heappop(minHeap)
        
        # The result list
        result = []
        # Drain the heap — a min-heap pops oldest-first, so res fills oldest → newest
        while minHeap:
            time, tweetId = heapq.heappop(minHeap)
            result.append(tweetId)
        # Reverse to get newest → oldest (the feed's order)
        result.reverse()

        # Return up to 10 tweet IDs, newest-first
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

     





        
