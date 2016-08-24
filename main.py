import webapp2
from views import *

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/create', CreateHandler),
    ('/edit', EditHandler),
    ('/createLoc', CreateLocHandler),
    ('/editLoc', EditLocHandler),
    ('/appIndex', appIndexHandler)
], debug=True)
