from models import ItemModel,LocationModel,LibraryModel
import datetime
from google.appengine.ext import ndb
from google.appengine.api import users

class Item(object):
	def save_item (self,title,typeof,release_date,copies,available,id):
		if id>0:
			item_k = ndb.Key('LibraryModel','Library','ItemModel',long(id))
			item = item_k.get()
		else:
			lib = LibraryModel(id='Library',name='My Library')
			lib.put()
			item = ItemModel(parent=lib.key)

		item.title = title
		item.typeof = typeof
		item.release_date = datetime.date(year=int(release_date[6:10]), month=int(release_date[3:5]), day=int(release_date[0:2]))
		item.copies = copies
		item.available = available
		item.user_name = users.get_current_user().email()
		item.put()

	def delete_item (self, item_ids):
		if len(item_ids)>0:
			for item_id in item_ids:
				item_k = ndb.Key('LibraryModel','Library','ItemModel',long(item_id))
				item = item_k.get
				item_k.delete()

	def list_item (self):
		lib = ndb.Key('LibraryModel','Library')
		# This is for full consistency vs eventual consistency
		#item_query = ItemModel.query()
		item_query = ItemModel.query(ancestor=lib)
		return item_query

class Location(object):
	def save_location (self,name,phone_number,id):
		if id>0:
			location_k = ndb.Key('LibraryModel','Library','LocationModel',long(id))
			location = location_k.get()
		else:
			lib = LibraryModel(id='Library',name='My Library')
			lib.put()
			location = LocationModel(parent=lib.key)

		location.name = name
		location.phone_number = phone_number
		location.user_name = users.get_current_user().email()
		location.put()

	def delete_location (self, location_ids):
		if len(location_ids)>0:
			for location_id in location_ids:
				location_k = ndb.Key('LibraryModel','Library','LocationModel',long(location_id))
				location = location_k.get
				location_k.delete()

	def list_location (self):
		lib = ndb.Key('LibraryModel','Library')
		location_query = LocationModel.query(ancestor=lib)
		return location_query