from models import ItemModel,LocationModel,LibraryModel
import datetime
from google.appengine.ext import ndb
from google.appengine.api import users

import endpoints
from google.appengine.ext import ndb
from protorpc import remote

from endpoints_proto_datastore.ndb import EndpointsModel

class Item(object):
	def save_item (self,title,typeof,release_date,location,available,id):
		if id>0:
			# make new key if there is no key
			item_k = ndb.Key('ItemModel',long(id))
			item = item_k.get()
		else:
			item = ItemModel()
		# get key
		location_k = ndb.Key('LocationModel',long(location))
		item.title = title
		item.typeof = typeof
		item.release_date = datetime.date(year=int(release_date[6:10]), month=int(release_date[3:5]), day=int(release_date[0:2]))
		item.location = location_k
		item.locationName = item.item_location
		item.available = available
		#item.user_name = users.get_current_user().email()
		item.put()

	def delete_item (self, item_ids):
		if len(item_ids)>0:
			for item_id in item_ids:
				item_k = ndb.Key('ItemModel',long(item_id))
				item = item_k.get
				item_k.delete()

	def list_item (self):
		#lib = ndb.Key('LibraryModel','Library')
		# This is for full consistency vs eventual consistency
		#item_query = ItemModel.query(ancestor=lib)
		# no ancestor, so this will be eventual consistency
		# get items for table
		item_query = ItemModel.query()
		return item_query

class Location(object):
	def save_location (self,name,phone_number,id):
		if id>0:
			location_k = ndb.Key('LocationModel',long(id))
			location = location_k.get()
		else:
			#lib = LibraryModel(id='Library',name='My Library')
			#lib.put()
			location = LocationModel()

		location.name = name
		location.phone_number = phone_number
		location.user_name = users.get_current_user().email()
		location.put()

	def delete_location (self, location_ids):
		if len(location_ids)>0:
			for location_id in location_ids:
				location_k = ndb.Key('LocationModel',long(location_id))
				location = location_k.get
				location_k.delete()

	def list_location (self):
		#lib = ndb.Key('LibraryModel','Library')
		# get locations for table
		location_query = LocationModel.query()
		return location_query