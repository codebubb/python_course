words = { "peripatetic" : "walking or traveling about",
          "inveigle" : "to entice, lure, or ensnare",
          "offing" : "the more distant part of the sea"
          }
for Alpha in range(1):
    print range(12,30) 



print words["offing"] ;


def d():
    define = words["peripatetic"]
    dic = raw_input("Would you like the definition of peripatetic? ").lower()
    if dic == "yes":
        print define 
    elif dic == "no":
        print "K"
        d()
d();

