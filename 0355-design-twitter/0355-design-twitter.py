class Twitter:

    def __init__(self):
        self.hashM = defaultdict(list)
        self.conn = defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.hashM[userId].append((self.count,tweetId,userId))
        self.count += 1
        for i in self.conn[userId]:
            self.hashM[i].append((self.count,tweetId,userId))
        self.count += 1
    def getNewsFeed(self, userId: int) -> list[int]:
        return [t[1] for t in heapq.nlargest(10, self.hashM[userId])]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId or followerId in self.conn[followeeId]:
            return
        self.conn[followeeId].add(followerId)
        for t in self.hashM[followeeId]:
            if t[2] == followeeId:
                self.hashM[followerId].append(t)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId or followerId not in self.conn[followeeId]:
            return
        self.conn[followeeId].discard(followerId)
        self.hashM[followerId] = [t for t in self.hashM[followerId] if t[2] != followeeId]
            


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)