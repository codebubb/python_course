
def isdate(text):
    if len(text) != 8:
        return False
    for i in range(0,2):
        if not text[i].isdigit():
            return False
    if text[2] != ':':
        return False
    for i in range(3,5):
        if not text[i].isdigit():
            return Fslse
    if text[5]!= ':':
        return False
    for i in range(6,8):
        if not text[i].isdigit():
            return False
    return True

doc = 'Title: New DocumentDocument time:Tue Jan  13 09:17:09\
2015Sustainable taxidermy iPhone, kitsch ennui tilde beard kogi\
photo booth skateboard shabby chic bitters cray. Gluten-free\
dreamcatcher flexitarian,  leggings  migas DIY narwhal fixie food\
truck shoreditch pour-over. +1 health goth 8-bit, tote bag pork \
belly intelligentsia  meh post-ironic polaroid  try-hard austin church-key.\
Pug hammock four dollar  toast cred, raw denim pitchfork  distillery.'

for c in range(0,len(doc)):
    find = doc[c:c+8]
    if isdate(find):
        if int(find[:2]) < 12:
            print 'This docmuent was printed in the morning'
        else:
            print 'This docmuent was printed in the afternoon..ish'
