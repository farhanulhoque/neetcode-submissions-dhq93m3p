class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        users = self.following[userId] | {userId}

        for u in users:
            for t in self.tweets[u]:
                heap.append(t)
        
        heapq.heapify(heap)

        result = heapq.nlargest(10, heap)

        return [tweetId for (time, tweetId) in result]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)



    # Solution Description: We need three pieces of state: each user's tweets (with timestamps, so we can order across users), each user's followees (a set), and a global timestamp counter that increments on every tweet (so tweets from different users are globally comparable by recency). postTweet appends (timestamp, tweetId) to the user's tweet list and bumps the timestamp. follow/unfollow add/remove from the followee set. The interesting one is getNewsFeed: gather the relevant users (followees + self), and merge their tweet lists to find the 10 most recent — a max-heap by timestamp does this efficiently, exactly like Merge k Sorted Lists.
        
