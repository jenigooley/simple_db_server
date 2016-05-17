import urlparse

#parse url for get and set keyvalues
def parse_for_keyvalue():
    url = "http://localhost:4000/set?somekey=somevalue"
    parsed_url  =  urlparse.urlsplit(url)
    print url
    p = parsed_url.path
    print "path:", p
    if p == "/set":
        print "store in memory"  

parse_for_keyvalue()
 

