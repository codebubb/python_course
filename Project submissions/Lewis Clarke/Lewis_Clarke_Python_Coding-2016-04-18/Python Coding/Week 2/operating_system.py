import os
print os.environ.keys()
user_input = raw_input("please choose the enviroment you wish to view from the list above")
print os.environ[user_input]
