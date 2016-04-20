#resources: lecture code
from google.appengine.ext import ndb
import webapp2
import db_models
import json
import string
import datetime
import time
from time import mktime

#to add course AND to view course(s)
class Course(webapp2.RequestHandler):
	def post(self):
		"""Creates a Course entity

		POST Body Variables
		name - Required. Coursename
		days - Required. Only letters allowed: MTWRF (Monday, Tuesday, Wednesday, ThuRsday, Friday)
		time - Required. 
		"""
		#create a new course to be added to database
		new_course = db_models.Course()
		name = self.request.get('name', default_value=None)
		days = self.request.get('days', default_value=None)
		time = self.request.get('time', default_value=None)

		#check to make sure required fields are entered correctly
        #if not, errors will be displayed
		if name:
			new_course.name = name
		else:
			self.response.status = 400
			self.response.status_message = "Error: Course Name Required."
		if days:	
			new_course.days = days
		else:
			self.response.status = 400
			self.response.status_message = "Error: Course Days Required."	
		if time:		
			new_course.time = time
		else:
			self.response.status = 400
			self.response.status_message = "Error: Course Time Required."

		#add course to database, get key.
		key = new_course.put()
		out = new_course.to_dict()
		self.response.write(out)
		return

	def get(self, **kwargs):
        #when specfic courseID (key) is entered, just display one course information
		if 'cid' in kwargs:
			out = ndb.Key(db_models.Course, int(kwargs['cid'])).get().to_dict()
			self.response.write(json.dumps(out))

		#when no specific key is entered then display out all keys in database
        #will display key, name, days, time
		else:
			q = db_models.Course.query()
			results = [{'key':x.key.id(), 'name':x.name, 'days':x.days, 'time':x.time} for x in q.fetch()]
			self.response.write(json.dumps(results))

#to update current course in database
class UpdateCourse(webapp2.RequestHandler):
	def post(self):
		# verify the application/json request
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "API service requires application/json"
			return
		
        #get course key(ID) 
		courseID = int(self.request.get('key'))
		course = db_models.Course().get_by_id(int(courseID))

		name = self.request.get('name', default_value=None)
		days = self.request.get('days', default_value=None)
		time = self.request.get('time', default_value=None)
				
		#if nothing is entered in fields, then nothing is altered
		if name:
			course.name = name
		if days:
			course.days = days
		if time:
			course.time = time
					
		key = course.put()
		out = course.to_dict()
		self.response.write(json.dumps(out))
		return

class DeleteCourse(webapp2.RequestHandler):
	def post(self):
		# verify the application/json request
		if 'application/json' not in self.request.accept:
		 	self.response.status = 406
		 	self.response.status_message = "API service requires application/json"
		 	return
		
        #get course key(ID) 
		courseID = int(self.request.get('key'))
		course = db_models.Course().get_by_id(int(courseID))
		course.key.delete()