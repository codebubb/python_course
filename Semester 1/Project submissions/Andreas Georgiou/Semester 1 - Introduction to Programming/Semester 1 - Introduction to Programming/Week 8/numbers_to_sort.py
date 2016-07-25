print "Use 'file.txt' as a sample file.", "\n"
file = raw_input("Enter your file name inclding the file ext. : ")

while True:
    try:
        with open(file, "r") as f:
            open_file = f.read()

        a_list = open_file.split()
        a_list = map(int, a_list)
        a_list.sort()
    
        for i in a_list:
            print i
        break
            
    except IOError:
        print "There is no file under the name of 'file.txt' to open."
        break
    except ValueError:
        print "The file you are using contains letter, it must consist of numbers only."
        break
