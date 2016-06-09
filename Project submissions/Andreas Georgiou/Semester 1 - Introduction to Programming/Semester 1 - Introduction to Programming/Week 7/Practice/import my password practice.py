import pickle

wfile = open('waiting.txt', 'r')

waiting_list = pickle.load(wfile)
wfile.close()
print waiting_list
