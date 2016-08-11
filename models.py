from google.appengine.ext import ndb

import endpoints
from google.appengine.ext import ndb
from protorpc import remote, message_types

from endpoints_proto_datastore.ndb import EndpointsModel

#Endpoints inherits from ndb, so it behaves similarily
class ItemModel (EndpointsModel):

	_message_fields_schema = ('id', 'title', 'typeof', 'release_date', 'available', 'location', 'locationName', 'locationID', 'username')

	timestamp = ndb.DateTimeProperty(auto_now=True)
	title = ndb.StringProperty()
	typeof = ndb.StringProperty()
	release_date = ndb.DateProperty()
	available = ndb.BooleanProperty()
	username = ndb.StringProperty()
	location = ndb.KeyProperty(kind='LocationModel')
	locationName = ndb.StringProperty()
	locationID = ndb.IntegerProperty()

	# function to return location name in table
	@property
	def item_location(self):
		return self.location.get().name

	@property
	def item_locationid(self):
		return self.location.get().id

class LocationModel (EndpointsModel):

	_message_fields_schema = ('id','name', 'phone_number', 'username')

	timestamp = ndb.DateTimeProperty(auto_now=True)
	username = ndb.StringProperty()
	phone_number = ndb.StringProperty()
	name = ndb.StringProperty()

class UserModel (EndpointsModel):
	
	_message_fields_schema = ('id','username', 'password')

	timestamp = ndb.DateTimeProperty(auto_now=True)
	username = ndb.StringProperty()
	password = ndb.StringProperty()

# API stuff
@endpoints.api(name='mylibrary', version='v1', description='CS496')
class LibraryApi(remote.Service):

	@ItemModel.method(path='newitem', http_method='POST', name='itemmodel.insert')
	def ItemModelInsert(self, item_model):
		# include all parameters to add item
		#if (not item_model.title or not item_model.typeof or not item_model.release_date or not item_model.available):
		#	raise endpoints.NotFoundException('Please supply all parameters.')
		item_model.put()
		item_model.location = ndb.Key('LocationModel',long(item_model.locationID))
		item_model.locationName = item_model.item_location
		item_model.put()
		return item_model

	@ItemModel.method(request_fields=('id',), path='itemmodel/{id}', http_method='GET', name='itemmodel.get')
	def ItemModelGet(self, item_model):
		if not item_model.from_datastore:
			raise endpoints.NotFoundException('Item not found.')
		return item_model

	@ItemModel.method(request_fields=('id',), response_message=message_types.VoidMessage, path='itemmodel/{id}', http_method='DELETE', name='itemmodel.delete')
	def ItemModelDelete(self, item_model):
		if not item_model.from_datastore:
			raise endpoints.NotFoundException('Item not found.')
		item_model._key.delete()
		return message_types.VoidMessage()

	@ItemModel.method(request_fields=('id','title', 'typeof', 'release_date', 'available', 'locationID','location', 'username'), path='itemmodel/{id}', http_method='PUT', name='itemmodel.put')
	def ItemModelPut(self, item_model):
		if not item_model.from_datastore:
			raise endpoints.NotFoundException('Item not found.')
		item_model.put()
		item_model.location = ndb.Key('LocationModel',long(item_model.locationID))
		item_model.locationName = item_model.item_location
		item_model.put()
		return item_model

	@ItemModel.query_method(query_fields=('limit', 'order', 'pageToken', 'username'), path='items', name='item.list')
	def ItemModelList(self, query):
		return query

	@LocationModel.method(path='newlocation', http_method='POST', name='locationmodel.insert')
	def LocationModelInsert(self, location_model):
		#include all parameters to add new location
		if (not location_model.name or not location_model.phone_number):
			raise endpoints.NotFoundException('Please supply all parameters.')
		location_model.put()
		return location_model

	@LocationModel.method(request_fields=('id',), path='locationmodel/{id}', http_method='GET', name='locationmodel.get')
	def LocationModelGet(self, location_model):
		if not location_model.from_datastore:
			raise endpoints.NotFoundException('Location not found.')
		return location_model

	@LocationModel.method(request_fields=('id',), response_message=message_types.VoidMessage, path='locationmodel/{id}', http_method='DELETE', name='locationmodel.delete')
	def LocationModelDelete(self, location_model):
		if not location_model.from_datastore:
			raise endpoints.NotFoundException('Location not found.')
		location_model._key.delete()
		return message_types.VoidMessage()

	@LocationModel.method(request_fields=('id','name', 'phone_number',), path='locationmodel/{id}', http_method='PUT', name='locationmodel.put')
	def LocationModelPut(self, location_model):
		if not location_model.from_datastore:
			raise endpoints.NotFoundException('Location not found.')
		location_model.put()
		return location_model

	@LocationModel.query_method(query_fields=('limit', 'order', 'pageToken'), path='locations', name='location.list')
	def LocationModelList(self, query):
		return query

	@UserModel.method(path='newuser', http_method='POST', name='usermodel.insert')
	def UserModelInsert(self, user_model):
		user_model.put()
		return user_model

	@UserModel.method(request_fields=('id',), path='usermodel/{id}', http_method='GET', name='usermodel.get')
	def UserModelGet(self, user_model):
		if not user_model.from_datastore:
			raise endpoints.NotFoundException('User not found.')
		return user_model

	@UserModel.query_method(query_fields=('limit', 'order', 'pageToken', 'username', 'password'), path='users', name='user.list')
	def UserModelList(self, query):
		return query

class LibraryModel (EndpointsModel):
	name = ndb.StringProperty()

application = endpoints.api_server([LibraryApi], restricted=False)