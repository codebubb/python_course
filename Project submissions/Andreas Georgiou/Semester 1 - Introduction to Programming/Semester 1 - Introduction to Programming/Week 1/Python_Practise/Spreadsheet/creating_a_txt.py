def new_txt():
    print('Creating new text file') 

    name = raw_input('Enter name of text file: ')+'.txt' # Name of text file coerced with +.txt

    try:
        file = open(name,'w') # Trying to create a new file or open one
        file.close()
        print name + " created"

    except:
        print('Something went wrong! Can\'t tell what?')

new_txt()
