#resources: class lectures

import datetime
import json
from time import mktime
from google.appengine.ext import ndb

class Model(ndb.Model):
    def to_dict(self):
        d = super(Model, self).to_dict()
        d['key'] = self.key.id()
        return d
    
#used for authenication and authorization (eventually)
class Register(Model):
    username = ndb.StringProperty()
    password = ndb.StringProperty()
    def to_dict(self):
        d = super(Register, self).to_dict()
        d['key'] = self.key.id()
        return d
    
#Student and Course have a relationship
class Student(Model):
    username = ndb.StringProperty()
    name = ndb.StringProperty()
    major = ndb.StringProperty()
    courses = ndb.KeyProperty(repeated=True)
    
    def to_dict(self):
        d = super(Student, self).to_dict()
        d['key'] = self.key.id()
        d['courses'] = [c.id() for c in d['courses']]
        return d

class Course(Model):
    name = ndb.StringProperty(required=True)
    days = ndb.StringProperty(required=True)
    time = ndb.StringProperty(required=True)
    
    def to_dict(self):
        d = super(Course, self).to_dict()
        d['key'] = self.key.id()
        return d
