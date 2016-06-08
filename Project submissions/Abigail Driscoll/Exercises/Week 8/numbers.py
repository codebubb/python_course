import os
import hashlib

f = open('file.txt', 'a')

rn = input("Please enter a number: ")


f.write(rn + '\n')