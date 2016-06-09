print ""
print "Encrypted login"
print ""
print "--------"

def cipher():
    print ""
    import codecs
    password = "cnffjbeq123"
    pw = raw_input("Enter your password: ").lower()
    pw_encrypted = codecs.encode(pw, "rot_13")
    print ""
    if pw_encrypted == password:
        print "Password accepted. Login in..."
    else:
        print ""
        print "You have entered an incorrect password. Try again."
        cipher()
    print "--"
    print "For test purposes the encrypted password(s) entered are printed below."
    print pw_encrypted

cipher()
