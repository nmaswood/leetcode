# --------------------------------- Structs ---------------------------------------------


class User():

	def __init__(self):

		self.name = 
		self._id = 
		self.feed = 
		self.followers = set()
		self.is_following = set()


class MailBox():

	def __init__(self, limit):

		self.read = Queue(size = int(limit * .75))
		self.unread = Queue(size = int(limit * .25))
		



class Mail():

	def __init__(self, rec, sender, time, content, opened = False):


		self.rec = rec
		self.sender = sender
		self.time = time
		self.content = content
		self.opened = opened


class Activity():

	def __init__(self, user_id, content_type, content):

		self.user_id =  user_id
		self.content_type =  content_type
		self.content = content

# --------------------------------- Methods ---------------------------------------------

class Twitter():

	def __init__(self,users):
		pass

	def a_follow_b(self,user_a, user_b):
		pass

	def a_unfollow_b(self,user_a, user_b):
		pass

	def broadcast(self, user_a, user_b):
		pass

class Utility():

	def __init__(self):
		pass

	def safe_remove(self, the_item, the_set):

		"""
		Any -> Set < Any> -> Int

		"""


		if the_item in the_set:

			the_set.remove(the_item)
			return 1

		return 0
















# from queue import Queue
# # Design a simplified version of Twitter where users can post tweets, follow/unfollow another user
# # and is able to see the 10 most recent tweets in the user's news feed.
# # Your design should support the following methods:

# # postTweet(userId, tweetId): Compose a new tweet.
# # getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed.
# # Each item in the news feed must be posted by users who the user followed or by the user herself. 
# # Tweets must be ordered from most recent to least recent.
# # follow(followerId, followeeId): Follower follows a followee.
# # unfollow(followerId, followeeId): Follower unfollows a followee.

# class User(object):

# 	def __init__(self):

# 		self.id = user_id
# 		self.feed = Queue(maxsize = 10)
# 		self.followers = set()
# 		self.followees = set()

# TWEET = 0;
# MSG = 1; 

# class Activity(object):

# 	def __init__(self,type,length,tags, content)
# 		self.type = type
# 		self.len = length
# 		self.tags = tags
# 		self.content = content

# 	def broadcast(self):
# 		pass

# class Tweet(object):
# 	def __init__(self):
# 		pass

# class Message(object):
# 	def __init__(self):
# 		pass

# class Twitter(object):

#     def __init__(self):
#     	self.users = user
#     	self.feed = feed
#     	self.followers = set()
#     	self.followee = set()


#     def postTweet(self, userId, tweetId):
#         """
#         Compose a new tweet.
#         :type userId: int
#         :type tweetId: int
#         :rtype: void
#         """
#         for follower in follwers:

#         	tweet.broadcast(userId, tweetId, follower)


#     def getNewsFeed(self, userId):
#         """
#         Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
#         :type userId: int
#         :rtype: List[int]
#         """

#         return list(users[userId].feed)
        

#     def follow(self, followerId, followeeId):

#         """
#         Follower follows a followee. If the operation is invalid, it should be a no-op.
#         :type followerId: int
#         :type followeeId: int
#         :rtype: void
#         """

#         users.[followerId].followee.add(followerId)
#         users.[followerId].follower.add(followeeId)


#     def unfollow(self, followerId, followeeId):
#         """
#         Follower unfollows a followee. If the operation is invalid, it should be a no-op.
#         :type followerId: int
#         :type followeeId: int
#         :rtype: void
#         """

# class Utility():

# 	def __init__(self):
# 		pass

# 	def safe_remove(self, the_set, item):

# 		if item in the_set:
# 			the_set.remove(item)
# 			return 0

# 		return -1






        


# # Your Twitter object will be instantiated and called as such:
# # obj = Twitter()
# # obj.postTweet(userId,tweetId)
# # param_2 = obj.getNewsFeed(userId)
# # obj.follow(followerId,followeeId)
# # obj.unfollow(followerId,followeeId)