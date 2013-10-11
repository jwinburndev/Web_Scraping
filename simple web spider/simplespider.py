#Christopher Reeves Web Scraping Tutorial
#simple web spider that returns array of urls. 
#http://youtube.com/creeveshft
#http://christopherreevesofficial.com
#http://twitter.com/cjreeves2011

import urllib
from bs4 import BeautifulSoup
import urlparse
import mechanize

url = "http://sparkbrowser.com"
br = mechanize.Browser()


urls = [url]
visited = [url]
while len(urls)>0:
    try:
        br.open(urls[0])
        urls.pop(0)
        for link in br.links():
            newurl =  urlparse.urljoin(link.base_url,link.url)
            #print newurl
            if newurl not in visited and url in newurl:
                visited.append(newurl)
                urls.append(newurl)
                print newurl
    except:
        print "error"
        urls.pop(0)
       
print visited
