#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import json
import urllib2
import urllib
import jinja2
import os
from snack import Snack
from user import User
from post import Post

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("templates/gif.html")
        query = self.request.get("search")
        index = self.request.get("index")
        if index == '':
            index = 0
        if query == '':
            query = "hello"
        base_url = "http://api.giphy.com/v1/gifs/search?"
        url_params = {'q': query , 'api_key': 'dc6zaTOxFJmzC', 'limit': 10}
        request_url = base_url + urllib.urlencode(url_params)
        giphy_response = urllib2.urlopen(request_url)
        giphy_json = giphy_response.read()
        giphy_data = json.loads(giphy_json)
        giphy_url = giphy_data['data'][0]['images']['original']['url']
        render_data = {}
        render_data['image_url'] = giphy_url
        self.response.write(template.render(render_data))
class SnackHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("templates/snack.html")
        snack_name = self.request.get("snack")
        snack_quantity = self.request.get("quantity")
        if snack_quantity == '':
            snack_quantity = 0
        self.response.write(template.render())
        my_snack = Snack(kind = snack_name, quantity = int(snack_quantity))
        my_snack.put()
class ListSnackHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("templates/snacklist.html")
        query = Snack.query()
        list_of_results = query.fetch()
        data = []
        render_data = {}
        for result in list_of_results:
            list_of_results_kind = result.kind
            data.append(list_of_results_kind)
        render_data["kind"] = data
        self.response.write(template.render(render_data))
class InstagramHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("templates/post.html")
        username = self.request.get("username")
        description = self.request.get("description")
        image_desc = self.request.get("image_description")
        query = Post.query()
        results = query.fetch()

        render_data = {}
        info = User(username = username, description = description, image_description = user_posted_by.image_description)
        info.put()
        self.response.write(template.render(render_data))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/snack', SnackHandler),
    ('/displaysnack', ListSnackHandler),
    ('/post', InstagramHandler)
], debug=True)
