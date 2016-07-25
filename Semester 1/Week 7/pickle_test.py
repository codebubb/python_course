import pickle

wfile = open('waiting.txt', 'r')
waiting_list = pickle.load(wfile)
wfile.close()
print waiting_list

new_patient = raw_input("Add new patient's name to list (leave blank for none):")
if new_patient:
    waiting_list.append(new_patient)
    wfile = open('waiting.txt', 'w')
    pickle.dump(waiting_list, wfile)
    wfile.close()
