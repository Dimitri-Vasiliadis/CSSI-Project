# from model import FacebookPost
# from random import randint
#
# #for x in range(5):
# #   post = FacebookPost(likes = randint(0, 10), comments =  "Test", name =
# #   "Dimitri", react = randint(0, 10), commentNum = randint(0, 10))
# #   post.put()
#
# query = FacebookPost.query()
# list_of_results = query.fetch()
#
# for post in list_of_results:
#     print post.likes

from google.appengine.ext import ndb

class FacebookPost(ndb.Model):
    likes = ndb.IntegerProperty()
    comments = ndb.StringProperty()
    name = ndb.StringProperty()
    react = ndb.IntegerProperty()
    commentNum = ndb.IntegerProperty()
