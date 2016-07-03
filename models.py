from google.appengine.ext import db

class ItemModel (db.Model):
	timestamp = db.DateTimeProperty(auto_now=True)
	title = db.StringProperty()
	typeof = db.StringProperty()
	release_date = db.DateProperty()
	copies = db.IntegerProperty()
	available = db.BooleanProperty()
	user_name = db.StringProperty()

class LibraryModel (db.Model):
	name = db.StringProperty()