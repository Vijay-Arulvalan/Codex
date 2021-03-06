class Users():
    def __init__(self, first_name, last_name, location, age,):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age
        self.full_name = first_name + ' ' + last_name
        self.login_attempts = 0

    def describe_user(self):
        print('\nThe user name is ' + self.full_name.title())
        print('The location of the user is ' + self.location.title())
        print('The age of the user is ' + str(self.age))

    def greet_user(self):
        print('\nHello, ' + self.full_name.title() + ', Its nice to hear from you.')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def read_login_attempts(self):
        print("The login_attempts are " + str(self.login_attempts))

user = Users('vijay', 'arulvalan', 'india', 24)
print("\nName: " + user.full_name.title() + "\nLocation: " + user.location.title() + "\nAge: " + str(user.age))
user.describe_user()
user.greet_user()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.reset_login_attempts()
user.read_login_attempts()
