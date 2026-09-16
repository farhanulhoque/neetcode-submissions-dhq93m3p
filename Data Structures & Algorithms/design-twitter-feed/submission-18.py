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
        for followeeId in self.following[userId]:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId]) - 1
                count, tweetId = self.tweets[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        
        while minHeap and len(result) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            result.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweets[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        # Follow: add to the follower's set
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Unfollow: discard (safe even if not present — no error)
        self.following[followerId].discard(followeeId)






