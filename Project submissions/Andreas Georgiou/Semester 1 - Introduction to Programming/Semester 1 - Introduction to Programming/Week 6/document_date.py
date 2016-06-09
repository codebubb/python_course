doc = """
Title: New Document
Document time: Tue Jan 13 10:17:09 2015
Sustainable taxidermy iPhone, kitsch ennui tilde beard kogi photo booth skateboard shabby chic bitters cray.
Gluten-free dreamcatcher flexitarian, leggings migas DIY narwhal fixie food truck shoreditch pour-over.
+1 health goth 8-bit, tote bag pork belly intelligentsia meh post-ironic polaroid try-hard austin church-key.
Pug hammock four dollar toast cred, raw denim pitchfork distillery.
"""

print doc

doc_list = doc.split()
time_int = []
time_01 = 0

for item in doc_list:
    if item == "10:17:09":
        time = item
        for num in time:
            if num.isdigit():
                time_int.append(num)

time_01 = time_int[0] + time_int[1]
time_01 = int(time_01)
    
print time
print time_int
print time_01

if time_01 >= 00 and time_01 < 12:
    print "This document was produced during the morning."
elif time_01 >= 12 and time_01 < 18:
    print "This document was produced during the afternoon."
elif time_01 >= 18 and time_01 <= 23:
    print "This document was produced during the evening."
else:
    print "testing"
