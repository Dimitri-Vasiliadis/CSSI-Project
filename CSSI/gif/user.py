from google.appengine.ext import ndb
from post import Post

class User(ndb.Model):
    username = ndb.StringProperty()
    description = ndb.StringProperty()
    posts = ndb.KeyProperty(Post, repeated = True)
