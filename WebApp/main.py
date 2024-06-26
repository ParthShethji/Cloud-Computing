import webapp2
from google.appengine.ext.webapp import template
import os
import urllib
import json

class MainPage(webapp2.RedirectHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), "index.html")
        context = {}
        self.response.out.write(template.render(path, context))

    def post(self):
        zipcode = self.request.get("zipCode")
        url = "https://api.postalpincode.in/pincode/" + zipcode
        data = urllib.urlopen(url).read()
        data = json.loads(data)
        post_office = data[0]['PostOffice'][0]['State']
        name = data[0]['PostOffice'][0]['Name']
        block = data[0]['PostOffice'][0]['Block']
        district = data[0]['PostOffice'][0]['District']
        template_values = {
            "post_office": post_office,
            "name": name,
            "block": block,
            "district": district
        }
        path = os.path.join(os.path.dirname(__file__), "results.html")
        self.response.out.write(template.render(path, template_values))

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)