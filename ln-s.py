#!/usr/bin/python
# Author: James Bertelson
# Email: catdevrandom@gmail.com
# Date: 10/28/2008
# Sends URLs to ln-s.net for shortening
# Revision History:
# 0.2: Switched from GET to POST
# 0.1: First release
#######################################

import urllib, urllib2, sys

#make HTTP Request
try:
	#Set up API
	url="http://ln-s.net/home/api.jsp"
	value={'url':sys.argv[1]}
	#Encode Request
	postdata=urllib.urlencode(value)
	#Send request
	request=urllib2.Request(url,postdata)
	response=urllib2.urlopen(request).read()
	
	#Handle response(and clean up newlines)
	if response[0:3]=="200":
		print response[4:].replace("\n", "")
	else:
		print response.replace("\n", "")

#Error Handling
except urllib2.HTTPError, e:
	print "Server Error"
	print 'Error code: ', e.code
except urllib2.URLError, e:
	print 'Connection Failed'
	print 'Reason: ', e.reason
except IndexError:
	print "Usage: ./ln-s.py http://urltoshorten.com/path/to/file"
except:
	print "Unknown Error"
