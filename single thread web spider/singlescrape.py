#Christopher Reeves Web Scraping Tutorial
#single threaded implimentation of a web spider
#http://youtube.com/creeveshft
#http://christopherreevesofficial.com
#http://twitter.com/cjreeves2011


import urllib
import re
import time
import MySQLdb
import mechanize
import readability
from bs4 import BeautifulSoup
from readability.readability import Document
import urlparse
import getarticle



class SingleScrape:
    visited = []
    urls = []
    articletexts = []
    external_links = []
    depth = 0
    counter = 0
    threadlist = []
    root = ""

    def __init__(self, url, depth):
       self.urls.append(url)
       self.visited.append(url)
       self.depth = depth
       self.root = url

   
    def run(self):
        while  len(self.urls)>0:     
            for r in self.urls:
                self.scrapeStep(r)
            self.urls = []
        return self.articletexts  

    def scrapeStep(self,root):
        br = mechanize.Browser()
        br.set_handle_robots(False)
        br.addheaders = [('User-agent', 'Firefox')]
        try:
            print "opening"+url
            html1 = br.open(root).read() 
            try:
                art_text = getarticle.getReadableArticle(root)
            except:
                print "PHAIL"
            for link in br.links():
                newurl =  urlparse.urljoin(link.base_url,link.url)
                if self.root in newurl.replace("www.","") and newurl not in self.visited:
                    self.urls.append(newurl) 
                    self.visited.append(newurl)
                    print newurl
        except:
            f = 0               



if __name__ == "__main__":
    url1 = "http://www.marketwatch.com/search?q=stocks"
    myfile = open("categorieslist.txt","w+")
    myfile.close()
    mysite = SingleScrape(url1,3)
    myarray =  mysite.run()

