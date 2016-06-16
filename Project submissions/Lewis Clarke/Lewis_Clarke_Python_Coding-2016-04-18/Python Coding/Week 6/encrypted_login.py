key = 'abcdefghijklmnopqrstuvwxyz'


def cipher():
    word = raw_input('Enter your password to encrypt: ')
    z = []
    for i in word:
        n = 13
        x = (key.index(i) - n) % 26
        y = key[x]
        z.append(str(y))
    print ''.join(z)


def decrypt():
    word = raw_input('Enter your password to decrypt: ')
    z = []
    for i in word:
        n = 13
        x = (key.index(i) + n) % 26
        y = key[x]
        z.append(str(y))
    print ''.join(z)


cipher()
decrypt()
