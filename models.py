from google.appengine.ext import ndb

class ItemModel (ndb.Model):
	timestamp = ndb.DateTimeProperty(auto_now=True)
	title = ndb.StringProperty()
	typeof = ndb.StringProperty()
	release_date = ndb.DateProperty()
	copies = ndb.IntegerProperty()
	available = ndb.BooleanProperty()
	user_name = ndb.StringProperty()

class LocationModel (ndb.Model):
	timestamp = ndb.DateTimeProperty(auto_now=True)
	user_name = ndb.StringProperty()
	name = ndb.StringProperty()
	phone_number = ndb.StringProperty()

class LibraryModel (ndb.Model):
	name = ndb.StringProperty()