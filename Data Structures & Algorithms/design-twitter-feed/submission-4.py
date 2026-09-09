from collections import OrderedDict
from typing import Dict, Set

class Twitter:

    def __init__(self):
        self.tweets_by_users = {}
        self.follows_for_user: Dict[int, Set[int]] = {}
        self.tweet_counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets_by_users:
            self.tweets_by_users[userId] = [(tweetId, self.tweet_counter)]
        else:
            self.tweets_by_users[userId].append((tweetId, self.tweet_counter))
        
        self.tweet_counter += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        all_tweets = []
        for u in (list(self.follows_for_user.get(userId, [])) + [userId]):
            all_tweets.extend(self.tweets_by_users.get(u, []))
        
        all_tweets.sort(key=lambda x: x[1], reverse=True)
        return [t[0] for t in all_tweets[:10]]


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return

        if followerId not in self.follows_for_user:
            self.follows_for_user[followerId] = {followeeId}
        else: 
            self.follows_for_user[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if (
            followerId == followeeId or 
            followerId not in self.follows_for_user or 
            followeeId not in self.follows_for_user[followerId]
        ): return
        
        self.follows_for_user[followerId].remove(followeeId)

        
