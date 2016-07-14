import webapp2
import cgi
import jinja2
import os

from datetime import datetime
from logics import Item
from google.appengine.ext import ndb
from google.appengine.api import users

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

jinja_environment.globals['year'] = datetime.now().year

class MainHandler(webapp2.RequestHandler):
    def get(self):
        item = Item() 
        template_values = {'items' : item.list_item()}
        template = jinja_environment.get_template('template/index.html')
        self.response.out.write(template.render(template_values))
    def post(self):
        user = users.get_current_user()
        if user:
            if self.request.POST.get('delete'):
                item_ids = self.request.get('item_id',allow_multiple=True)
                item = Item()
                item.delete_item(item_ids)
                self.redirect('/')
        else:
            self.redirect(users.create_login_url(self.request.uri))

class CreateHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            template = jinja_environment.get_template('template/create.html')
            self.response.out.write(template.render())
        else:
            self.redirect(users.create_login_url(self.request.uri))
    def post(self):
        input_title = self.request.get('title').strip()
        input_typeof = self.request.get('typeof').strip()
        input_release_date = self.request.get('release_date').strip()
        input_copies = int(self.request.get('copies').strip())
        input_available = self.request.get('available').strip() != ''
   
        item = Item()
        item.save_item(input_title,input_typeof,input_release_date,input_copies,input_available,0)
        self.redirect('/create')


class EditHandler(webapp2.RequestHandler):
    def get (self):
        user = users.get_current_user()
        if user:
            # get ID of entity Key
            item_k = ndb.Key('LibraryModel','Library','ItemModel',long(self.request.get('id')))
            # get entity from key instance
            item = item_k.get()
            
            template_values = {'item' : item}
            template = jinja_environment.get_template('template/edit.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(users.create_login_url(self.request.uri))
    def post(self):
        input_id = self.request.get('id')
        input_title = self.request.get('title').strip()
        input_typeof = self.request.get('typeof').strip()
        input_release_date = self.request.get('release_date').strip()
        input_copies = int(self.request.get('copies').strip())
        input_available = self.request.get('available').strip() != ''

        item = Item()
        item.save_item (input_title,input_typeof,input_release_date,input_copies,input_available,long(input_id))
        self.redirect('/')