#this will render the content to a particular path

import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write("Hello World I am from VIT")

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)