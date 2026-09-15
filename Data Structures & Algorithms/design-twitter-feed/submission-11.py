class Twitter:
    # Optimized version of the first solution (bounded-heap getNewsFeed)

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
        # Heap to merge tweets from all relevant users
        heap = []

        # The relevant users = who they follow plus themself (| {userId})
        users = self.following[userId] | {userId}

        # Collect all tweets from those users into the heap
        for u in users:
            # only the last 10 tweets of each user can matter
            for t in self.tweets[u][-10:]:
                heap.append(t)
        
        return [tweetId for (time, tweetId) in heapq.nlargest(10, heap)]

    def follow(self, followerId: int, followeeId: int) -> None:
        # Follow: add to the follower's set
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Unfollow: discard (safe even if not present — no error)
        self.following[followerId].discard(followeeId)


    # O(F) time, O(F) space — much better when users have MANY tweets. Take the last 10 tweets from each of the F users → O(F × 10) = O(F) time. Merge those with a size-10 heap → O(F log 10) = O(F) space.

    # getNewsFeed: since each user's tweets are already sorted by time, you only need each followee's most recent 10 tweets (older ones can't possibly make the global top 10). Merging those with a size-10 heap gives O(F log 10) = O(F) instead of O(N) — a big win when users have thousands of tweets.

    # self.tweets[u][-10:] grabs just each user's latest 10 tweets. Since tweets are time-sorted, older ones can't reach the global top 10 — so we skip them. This bounds the work to O(F × 10) regardless of how many tweets each user has.



