try: 
    from googlesearch import search 
    
except ImportError:  
    print("No module named 'google' found") 
  
# to search 
keyword = raw_input("Enter a Keyword:")

Organization = raw_input("Enter the organization:")

query = keyword+"/"+Organization+ ".pdf"

  
for j in search(query, tld="com", num=25, stop=1, pause=2):
    if j[-4:]==".pdf":
        print j
    else: 
        print("Not Found")
	continue
print "\n"
print "Searching for External Sources"
try:

    for j in search(query, tld="co.in", num=100, stop=1,pause=2):    
        if j[-4:]==".pdf":
            print j
        else:
            continue
except:
    print "Not Found"


try:

    for j in search(query, tld="org.ai", num=25, stop=1,pause=2):    
        if j[-4:]==".pdf":
            print j
        else:
            continue
except:
    print "Not Found"

try:

    for j in search(query, tld="edu.ac", num=25, stop=1,pause=2):    
        if j[-4:]==".pdf":
            print j
        else:
            continue
except:
    print "Not Found"
#photo giggle wish cupboard enact student trend zebra head group wise torch
