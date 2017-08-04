from google.appengine.ext import ndb

class Snack(ndb.Model):
    kind = ndb.StringProperty(required = True)
    rating = ndb.IntegerProperty(repeated = True)
    quantity = ndb.IntegerProperty()
    calories = ndb.IntegerProperty()
    expiration = ndb.DateProperty()
