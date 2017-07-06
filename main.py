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
import jinja2
import os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')rt5yr5e6y
        templates = jinja_environment.get_template('templateproject.html')

class NextHandler(webapp2.RequestHandler):

    def get(self):
        guestbook_name = self.request.get('madlib')
        #dictionary= {'Adjective, Noun, Name, Verb, Number, Color '}
        dictionary= {'noun': self.request.get}
        app = webapp2.WSGIApplication
        templates = jinja_environment.get_template('templateproject.html')
        self.response.write(templates.render(dictionary))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/action_page', NextHandler)
], debug=True)
