import urllib2
response = urllib2.urlopen('http://www.apvocab.com/')
html = response.read()
print html