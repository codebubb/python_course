def rot13(n):
    o=""
    key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u',
           'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
           'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
           'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S',
           'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A',
           'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I',
           'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
    for x in n:
        v = x in key.keys()
        if v==True:
            o+=(key[x])
    return o

#password = rot13(input("Please enter your password here: "))
#print(password)
#rot13(password)

def position(n):
    o=""
    key = {'A':'1', 'B':'2', 'C':'3', 'D':'4', 'E':'5', 'F':'6', 'G':'7', 'H':'8',
           'I':'9', 'J':'10', 'K':'11', 'L':'12', 'M':'13', 'N':'14', 'O':'15', 'P':'16',
           'Q':'17', 'R':'18', 'S':'19', 'T':'20', 'U':'21', 'V':'22', 'W':'23', 'X':'24',
           'Y':'25', 'Z':'26', 'a':'1', 'b':'2', 'c':'3', 'd':'4', 'e':'5', 'f':'6', 'g':'7',
           'h':'8', 'i':'9', 'j':'10', 'k':'11', 'l':'12', 'm':'13', 'n':'14', 'o':'15', 'p':'16',
           'q':'17', 'r':'18', 's':'19', 't':'20', 'u':'21', 'v':'22', 'w':'23', 'x':'24', 'y':'25', 'z':'26'}
    for x in n:
        v = x in key.keys()
        if v==True:
            o+=(key[x])
        else:
            o+=x
    return o
#Yes= position(input("Please enter a letter of the alphabet: "))
#print(Yes)



def alength():
    string = input("Please enter a list of words: ") + " "
    length = len(string)
    spaces = string.count(" ")
    words = length - spaces
    average = (words)/(spaces)
    print(average)

alength()

