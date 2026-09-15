import heapq
from collections import defaultdict

class Twitter:
    def __init__(self):
        self.time = 0                                # Line 1
        self.tweets = defaultdict(list)  # userId -> [(time, tweetId)]   # Line 2
        self.following = defaultdict(set)  # userId -> {followeeIds}      # Line 3

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))   # Line 4
        self.time += 1                               # Line 5

    def getNewsFeed(self, userId: int) -> list[int]:
        heap = []                                    # Line 6

        # the user sees their own tweets + those they follow
        users = self.following[userId] | {userId}    # Line 7

        for u in users:                              # Line 8
            for t in self.tweets[u]:                 # Line 9
                heap.append(t)                       # Line 10

        # max-heap by time: negate, take 10 largest
        heapq.heapify(heap)                          # Line 11 (min-heap of all)
        # get the 10 most recent (largest timestamps)
        res = heapq.nlargest(10, heap)               # Line 12

        return [tweetId for (time, tweetId) in res]  # Line 13

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)   # Line 14

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)  # Line 15