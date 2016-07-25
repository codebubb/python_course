import urllib

def page_exists(url):
    page = urllib.urlopen(url)
    return True if page.code == 200 else False
page_to_check = 'http://bbc.co.uk/'
print "Does" ,page_to_check ,"exist?", page_exists(page_to_check)
