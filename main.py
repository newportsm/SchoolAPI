# Sarah Newport
# CS 496 - HW3: Part 2
# School API

# resources: class lectures

import webapp2
from google.appengine.api import oauth

app = webapp2.WSGIApplication([
	('/course', 'course.Course'),
	], debug=True)
#app.router.add(webapp2.Route(r'/login', 'student.Login'))
#app.router.add(webapp2.Route(r'/register', 'student.Register'))
app.router.add(webapp2.Route(r'/course/<cid:[0-9]+>', 'course.Course'))
app.router.add(webapp2.Route(r'/updateCourse', 'course.UpdateCourse'))
app.router.add(webapp2.Route(r'/deleteCourse', 'course.DeleteCourse'))
app.router.add(webapp2.Route(r'/updateStudent', 'student.UpdateStudent'))
app.router.add(webapp2.Route(r'/deleteStudent', 'student.DeleteStudent'))
app.router.add(webapp2.Route(r'/student', 'student.Student'))
app.router.add(webapp2.Route(r'/student/<sid:[0-9]+>', 'student.Student'))
app.router.add(webapp2.Route(r'/student/<sid:[0-9]+>/course/<cid:[0-9]+>', 'student.StudentCourses'))
app.router.add(webapp2.Route(r'/delete/student/<sid:[0-9]+>/course/<cid:[0-9]+>', 'student.StudentCourseDelete'))
app.router.add(webapp2.Route(r'/student/<sid:[0-9]+>/deleteCourse/<cid:[0-9]+>', 'student.StudentDelCourse'))