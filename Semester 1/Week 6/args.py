#args / kwargs

def sum_list(*list_in):
    total = 0
    for i in list_in:
        total += i
    print "Total is:", total

sum_list(1,2,3)
print

def exam_results(**dict_in):
    print "Subject\t\tResult"
    print "-"*24
    for k,v in dict_in.iteritems():
        print k,"\t",v

exam_results(English=60, Mathematics=70, Science=86)
