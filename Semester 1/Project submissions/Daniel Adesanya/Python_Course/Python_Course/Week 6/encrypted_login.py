def p():
    password = raw_input("Please Enter Your Passphrase ").lower
    import codecs
    codecs.encode('foobar', 'rot_13')
    if password == " ":
        print "Encripted"
    p()
p()

