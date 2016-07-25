import re

def get_hour_of_day(str):
    time = re.search('([0-9]{1,2}:?){3}', str)
    return int(time.group(0)[0:2])

def get_text_time(hour):
    if hour > 17:
        return "Evening"
    elif hour > 11:
        return "Afternoon"
    else:
        return "Morning"

str = '''
Title: New Document
Document time: Tue Jan 13 18:17:09 2015
Sustainable taxidermy iPhone, kitsch ennui tilde beard kogi photo booth skateboard shabby chic bitters cray. Gluten-free dreamcatcher flexitarian, leggings migas DIY narwhal fixie food truck shoreditch pour-over. +1 health goth 8-bit, tote bag pork belly intelligentsia meh post-ironic polaroid try-hard austin church-key. Pug hammock four dollar toast cred, raw denim pitchfork distillery.
'''

print str
print "The document was created in the", get_text_time(get_hour_of_day(str))
