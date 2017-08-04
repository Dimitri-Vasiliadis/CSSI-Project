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
import jinja2
import os
import webapp2
from random import randint

#set up environment for Jinja
#this sets jinja's relative directory to match the directory name(dirname) of
#the current __file__, in this case, main.py
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def code(self):
        greeting_list = ["Hello!", "Whats up!", "How are you?"]
        text = ""
        for x in range(randint(1, 5)):
            text += greeting_list[randint(0, len(greeting_list)-1)]
        return text
    def get(self):
        number =  int(self.request.get("number"))
        word = self.request.get("word")
        #response_html = self.code()
        #self.response.write(response_html)
        for x in range(number):
            self.response.write(" " + word)

class MilkHandler(webapp2.RequestHandler):
    def get(self):
        number =  self.request.get("number")
        self.response.write("Go get some milk!" + produce)

class ImageHandler(webapp2.RequestHandler):
    def get(self):
        my_template = jinja_environment.get_template("templates/hello-world.html")
        my_name = self.request.get("my_name_from_url")
        veg = self.request.get("vegetable_from_url")
        times = self.request.get("steve_from_url")
        render_data = {
            "greeting" : "Hello"
        }
        #[] tell you what to refer to in the HTML and after the equals sign is the variable from above that you get from the URL
        render_data["name"] = my_name
        render_data["vegetable"] = veg
        render_data["number"] = int(times)
        self.response.write(my_template.render(render_data))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/milk', MilkHandler),
    ('/image', ImageHandler)
], debug=True)
