# Single level
class User:

    def login(self):
        print('Login')
    def register(self):
        print('Register')

class Student(User): #inheritance

    def enroll(self):
        print('Enroll')
    def review(self):
        print('Review')

student1= Student()
#allowed to inherit from parent
student1.register()
student1.login()
student1.enroll()

# parent cannot inherit from child
u = User()
u.register()
u.login()
