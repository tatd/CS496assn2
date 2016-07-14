from google.appengine.ext import ndb

class ItemModel (ndb.Model):
	timestamp = ndb.DateTimeProperty(auto_now=True)
	title = ndb.StringProperty()
	typeof = ndb.StringProperty()
	release_date = ndb.DateProperty()
	copies = ndb.IntegerProperty()
	available = ndb.BooleanProperty()
	user_name = ndb.StringProperty()

class LibraryModel (ndb.Model):
	name = ndb.StringProperty()