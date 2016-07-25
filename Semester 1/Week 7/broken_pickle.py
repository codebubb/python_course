import pickle

with open('password.txt', 'r') as f:
    password = pickle.load(f)

print password
