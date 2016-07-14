from google.appengine.ext import ndb

class ItemModel (ndb.Model):
	timestamp = ndb.DateTimeProperty(auto_now=True)
	title = ndb.StringProperty()
	typeof = ndb.StringProperty()
	release_date = ndb.DateProperty()
	available = ndb.BooleanProperty()
	user_name = ndb.StringProperty()
	location = ndb.KeyProperty(kind='LocationModel')
	@property
	def item_location(self):
		return self.location.get().name
	

class LocationModel (ndb.Model):
	timestamp = ndb.DateTimeProperty(auto_now=True)
	user_name = ndb.StringProperty()
	phone_number = ndb.StringProperty()
	name = ndb.StringProperty()

class LibraryModel (ndb.Model):
	name = ndb.StringProperty()