class User():
    def __init__(self, name, pwd):
        self.username = name
        self.password = pwd

    def authenticated(self):
        return self.password == 'password'


james = User('jbubb', 'password')

print james.username, james.password



#######
if james.authenticated():
    print "User is logged in"
else:
    print "you are not allowed to do that!"
