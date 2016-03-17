import webapp2
from google.appengine.api import users

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
  ('/a/.*', AuthPage), 
  ('[^a].*', MainPage),
  ], debug=True)
