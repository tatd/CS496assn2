import webapp2
import cgi
import jinja2
import os

from datetime import datetime
from logics import Item, Location
from google.appengine.ext import ndb
from google.appengine.api import users

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

jinja_environment.globals['year'] = datetime.now().year

class MainHandler(webapp2.RequestHandler):
    def get(self):
        item = Item()
        location = Location() 
        template_values = {'items' : item.list_item(), 'locations' : location.list_location()}
        template = jinja_environment.get_template('template/index.html')
        self.response.out.write(template.render(template_values))
    def post(self):
        user = users.get_current_user()
        if user:
            if self.request.POST.get('delete'):
                item_ids = self.request.get_all('item_id')
                item = Item()
                item.delete_item(item_ids)
                location_ids = self.request.get_all('location_id')
                location = Location()
                location.delete_location(location_ids)
                self.redirect('/')
        else:
            self.redirect(users.create_login_url(self.request.uri))

class CreateHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            item = Item()
            location = Location() 
            template_values = {'items' : item.list_item(), 'locations' : location.list_location()}
            template = jinja_environment.get_template('template/create.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(users.create_login_url(self.request.uri))
    def post(self):

        input_title = self.request.get('title').strip()
        input_typeof = self.request.get('typeof').strip()
        input_release_date = self.request.get('release_date').strip()
        input_location = self.request.get('location')
        input_available = self.request.get('available').strip() != ''
   
        item = Item()
        item.save_item(input_title,input_typeof,input_release_date,long(input_location),input_available,0)
        self.redirect('/create')


class EditHandler(webapp2.RequestHandler):
    def get (self):
        user = users.get_current_user()
        if user:
            # get ID of entity Key
            item_k = ndb.Key('LibraryModel','Library','ItemModel',long(self.request.get('id')))
            # get entity from key instance
            item = item_k.get()
            
            location = Location()
            template_values = {'item' : item, 'locations' : location.list_location()}
            template = jinja_environment.get_template('template/edit.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(users.create_login_url(self.request.uri))
    def post(self):
        input_id = self.request.get('id')
        input_title = self.request.get('title').strip()
        input_typeof = self.request.get('typeof').strip()
        input_release_date = self.request.get('release_date').strip()
        input_location = self.request.get('location')
        input_available = self.request.get('available').strip() != ''

        item = Item()
        item.save_item (input_title,input_typeof,input_release_date,long(input_location),input_available,long(input_id))
        self.redirect('/')

class CreateLocHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            template = jinja_environment.get_template('template/createLoc.html')
            self.response.out.write(template.render())
        else:
            self.redirect(users.create_login_url(self.request.uri))
    def post(self):
        input_name = self.request.get('name').strip()
        input_phone_number = self.request.get('phone_number').strip()
   
        location = Location()
        location.save_location(input_name,input_phone_number,0)
        self.redirect('/createLoc')


class EditLocHandler(webapp2.RequestHandler):
    def get (self):
        user = users.get_current_user()
        if user:
            # get ID of entity Key
            location_k = ndb.Key('LibraryModel','Library','LocationModel',long(self.request.get('id')))
            # get entity from key instance
            location = location_k.get()
            
            template_values = {'location' : location}
            template = jinja_environment.get_template('template/editLoc.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(users.create_login_url(self.request.uri))
    def post(self):
        input_id = self.request.get('id')
        input_name = self.request.get('name').strip()
        input_phone_number = self.request.get('phone_number').strip()

        location = Location()
        location.save_location (input_name,input_phone_number,long(input_id))
        self.redirect('/')