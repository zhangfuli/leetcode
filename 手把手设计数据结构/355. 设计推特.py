import time


class User:
    def __init__(self, userId=None):
        self.userId = userId
        self.followee = []
        self.tweet = []

    def addTweet(self, tweetId):
        self.tweet.append([tweetId, time.time()])

    def addFollow(self, followeeId):
        if followeeId not in self.followee:
            self.followee.append(followeeId)

    def removeFollow(self, followeeId):
        if followeeId in self.followee:
            self.followee.remove(followeeId)

    def getTweet(self):
        return self.tweet

    def getFollow(self):
        return self.followee


class Twitter:
    def __init__(self):
        self.hashmap = {}

    def postTweet(self, userId, tweetId) -> None:
        """
        Compose a new tweet.
        """
        if userId in self.hashmap:
            user = self.hashmap[userId]
        else:
            user = User(userId)
            self.hashmap[userId] = user
        user.addTweet(tweetId)

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        if userId in self.hashmap:
            user = self.hashmap[userId]
        else:
            return []
        tweet = user.getTweet().copy()
        followee = user.getFollow()
        for followeeID in followee:
            if followeeID in self.hashmap:
                tweet += self.hashmap[followeeID].getTweet()
            else:
                tweet += []

        tweet_sort = sorted(tweet, key=lambda d: -d[1])
        result = [tweet_sort[i][0] for i in range(len(tweet_sort))]
        if len(result) > 10:
            return result[:10]
        else:
            return result

    def follow(self, followerId, followeeId) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.hashmap:
            user = self.hashmap[followerId]
        else:
            user = User(followerId)
            self.hashmap[followerId] = User(followerId)
        user.addFollow(followeeId)
        self.hashmap[followerId] = user

    def unfollow(self, followerId, followeeId) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        user = self.hashmap[followerId]
        user.removeFollow(followeeId)


# Your Twitter object will be instantiated and called as such:
twitter = Twitter()
twitter.follow(1, 5)
print(twitter.getNewsFeed(1))
