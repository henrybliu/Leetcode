from collections import defaultdict
import heapq


class Twitter:
    """
    Use a hashmap to map who follows who. Have one large max heap with the
    timestamps associated to when each tweet is created. Also associate tweets
    with the userId to identify the 10 most recent tweets belonging to a user
    or who they follow.

    Time: O(nlogn) for getNewsFeed(), O(1) for __init__(), O(logn) for
    postTweet, O(1) for follow() and unfollow()
    Space: O(n + m)
    where n are the tweets and m the users
    """

    def __init__(self):
        self.h = []
        self.follows = defaultdict(set)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.h, (-self.timestamp, userId, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        popped = []
        res = []

        while self.h and len(res) < 10:
            timestamp, poster, tweetId = heapq.heappop(self.h)
            popped.append((timestamp, poster, tweetId))
            if poster == userId or poster in self.follows[userId]:
                res.append(tweetId)

        # add back what was popped to the overall heap
        for pop in popped:
            heapq.heappush(self.h, pop)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
