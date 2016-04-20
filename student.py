#resources: lecture code

import webapp2
import db_models
import json
from google.appengine.ext import ndb


#authenication/authorization currently commented out. 
#the bones are there to build off of
"""

#to register for login procedure
class Register(webapp2.RequestHandler):
    def post(self):
        
        new_user = db_models.Register()
        username = self.request.get('username', default_value=None)
        password = self.request.get('password', default_value=None)
        
        #username is supplied for registration
        if username:
            user_exists = [u.username for u in db_models.Register.query(db_models.Register.username == username).fetch()]
            
            #error: username not unique in database
            if username in user_exists:
                #no password entered
                if not password:
                    self.response.status = 400
                    self.response.status_message = "Username is already taken and no password entered."
                else:
                    self.response.status = 400
                    self.response.status_message = "Username is already taken, pleae enter new Username."
            #username is unique in database
            else:
                #no password is entered
                if not password:
                    self.response.status = 400
                    self.response.status_message = "Need to enter password."
                    
                #username and password are entered successfully into database
                else:
                    new_user.username = username
                    new_user.password = password
                    
                    key = new_user.put()
                    out = new_user.to_dict()
                    self.response.write(json.dumps(out))
        return
    
class Login(webapp2.RequestHandler):
    def post(self):
        new_user = db.models.Register()
        username = self.request.get('username', default_value=None)
        password = self.request.get('password', default_value=None)
        user_exists = []
        
        #username is supplied
        if username:
            user_exists = [u.username for u in db.models.Register.query(db.models.Register.username == username).fetch()]
            
            #username is found in database
            if username in user_exists:
                #the password is not entered
                if not password:
                    self.response.status = 400
                    self.response.status_message = "Incorrect Password entered"
                else:
                    user_match = db_models.Register.query(db_models.Register.username == username).fetch()
                    #password is a match
                    if password == user_match[0].password:
                        self.response.write(json.dumps({'username': user_match[0].username}))
                    #password incorrect
                    else:
                        self.response.status = 410
                        self.response.status_message = "Incorrect Password entered."
            else:
                self.response.status = 400
        else:
            self.response.status = 400
            self.response.status_message = "Username does not exist, please register first."
        return
"""


class Student(webapp2.RequestHandler):
    def post(self):
        new_student = db_models.Student()
        username = self.request.get('username', default_value=None)
        name = self.request.get('name', default_value=None)
        major = self.request.get('major', default_value=None)
        courses = self.request.get_all('courses[]', default_value=None)
        
        if username:
            new_student.username = username
        if name:
            new_student.name = name
        if major:
            new_student.major = major
        if courses:
            for course in courses:
                new_student.courses.append(ndb.Key(db_models.Course, int(course)))
        key = new_student.put()
        out = new_student.to_dict()
        self.response.write(json.dumps(out))
        return
    
    def get(self, **kwargs):
        #when specific key is entered
        if 'sid' in kwargs:
            out = ndb.Key(db_models.Student, int(kwargs['sid'])).get().to_dict()
            self.response.write(json.dumps(out))
            
        #if no id is entered, then display all keys
        else:
            q = db_models.Student.query()
            results = [{'key':x.key.id(), 'username':x.username, 'name':x.name, 'major':x.major} for x in q.fetch()]
            self.response.write(json.dumps(results))
            
class UpdateStudent(webapp2.RequestHandler):
    def post(self):
        #get the student key
        studentID = int(self.request.get('key'))
        student = db_models.Student().get_by_id(int(studentID))
        
        name = self.request.get('name', default_value=None)
        major = self.request.get('major', default_value=None)
        courses = self.request.get('courses[]', default_value=None)
        
        #no changes are made to additional fields
        if name:
            student.name = name
        if major:
            student.major = major
        if courses:
            for c in courses:
                student.courses.append(ndb.Key(db_models.Course,int(courses)))
                
        key = student.put()
        out = student.to_dict()
        self.response.write(json.dumps(out))
        return
    
class DeleteStudent(webapp2.RequestHandler):
    def post(self):
        #get studentID
        studentID = int(self.request.get('key'))
        student = db_models.Student().get_by_id(int(studentID))
        student.key.delete()

class StudentCourses(webapp2.RequestHandler):
    def put(self, **kwargs):
        if 'sid' in kwargs:
            student = ndb.Key(db_models.Student, int(kwargs['sid'])).get()
            if not student:
                self.response.status = 404
                self.response.status_message = "Student Not Found, Please Add Student."
                return
        if 'cid' in kwargs:
            course = ndb.Key(db_models.Course, int(kwargs['cid']))
            if not student:
                self.response.status = 404
                self.response.status_message = "Course Not Found, Please Add Appropriate Course."
                return
        if course not in student.courses:
            student.courses.append(course)
            student.put()
        self.response.write(json.dumps(student.to_dict()))
        return

class StudentCourseDelete(webapp2.RequestHandler):
    def delete(self, **kwargs):
        if 'sid' in kwargs:
            student = ndb.Key(db_models.Student, int(kwargs['sid'])).get()
            if not studnet:
                self.response.status = 404
                self.response.status_message = "Student Not Found. Please enter correct StudentID."
                return
        if 'cid' in kwargs:
            course = ndb.Key(db_models.Course, int(kwargs['cid']))
            if not student:
                self.response.status = 404
                self.response.status_message = "Course Not Found. Please enter correct CourseID."
                return
        for c in student.courses:
            student.courses.append(course)
            student.put()
            student.courses.remove(c)
        self.response.write(student.courses[0])
        s = student.query()
        self.response(s)
        for c in student.courses:
            self.response.write(json.dumps(student_courses))
        return