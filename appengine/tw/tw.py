import os
import urllib
import json

from google.appengine.api import users

import jinja2
import webapp2

import model


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(
      os.path.join(os.path.dirname(__file__), 'templates')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class TweetsApi(webapp2.RequestHandler):
  def get(self):
    json_txt = json.dumps([p.to_d() for p in model.Message.query_message().fetch()])
    self.response.headers['Content-Type'] = "application/json; charset=utf-8"
    self.response.write(json_txt)

  def post(self):
    text = self.request.get("text")
    msg = model.Message(text=text, parent=model.DEFAULT_MSG_KEY)
    msg.put()
    self.get()


class FrontPage(webapp2.RequestHandler):
  def get(self):
    template = JINJA_ENVIRONMENT.get_template('index.html')
    self.response.write(template.render({}))

class AuthPage(webapp2.RequestHandler):
  def get(self):
    user = users.get_current_user()
    if user:
        greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
          (user.nickname(), users.create_logout_url('/')))
    else:
        greeting = ('<a href="%s">Sign in or register</a>.' %
          users.create_login_url(self.request.path_qs))

    self.response.out.write('<html><body>%s</body></html>' % greeting)


class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.write('Hello, "%s"!' % self.request.path_qs)


app = webapp2.WSGIApplication([
  ('/tw/', TweetsApi),
  ('/a/.*', AuthPage), 
  ('/', FrontPage),
  ], debug=True)
