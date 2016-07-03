from models import ItemModel,LibraryModel
import datetime
from google.appengine.ext import db
from google.appengine.api import users

class Item(object):
	def save_item (self,title,typeof,release_date,copies,available,id):
		if id>0:
			item_k = db.Key.from_path('LibraryModel','Library','ItemModel',long(id))
			item = db.get(item_k)
		else:
			lib = LibraryModel(key_name='Library',name='My Library')
			lib.put()
			item = ItemModel(parent = lib)

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
				item_k = db.Key.from_path('LibraryModel','Library','ItemModel',long(item_id))
				item = db.get(item_k)
				db.delete(item_k)

	def list_item (self):
		lib = db.Key.from_path('LibraryModel','Library')
		item_query = ItemModel.all()
		item_query.ancestor(lib)
		return item_query