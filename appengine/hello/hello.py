import webapp2

class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.write('Hello, "%s"!' % self.request.path_qs)

app = webapp2.WSGIApplication([
  ('/.*', MainPage),], 
debug=True)
