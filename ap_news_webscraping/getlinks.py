#Christopher Reeves Web Scraping Tutorial
#getting page source with python
#http://youtube.com/creeveshft
#http://christopherreevesofficial.com
#http://twitter.com/cjreeves2011

import urllib
import mechanize
from bs4 import BeautifulSoup
import MySQLdb
import datetime



def searchAP(searchterm):
    newlinks = []
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.addheaders = [('User-agent', 'Firefox')]
    text = ""
    start = 0
    while "There were no matches for your search" not in text:
        url = "http://hosted.ap.org/dynamic/external/search.hosted.ap.org/wireCoreTool/Search?SITE=AP&SECTION=HOME&TEMPLATE=DEFAULT&start_at="+str(start)+"&query="+searchterm
        text = urllib.urlopen(url).read()
        soup = BeautifulSoup(text)

        

        results = soup.findAll('a')
        for r in results:
            if "TEMPLATE=DEFAULT" in r['href'] and "/dynamic" in r["href"]:
                newlinks.append("http://hosted.ap.org"+ str(r["href"]))
        start +=25

    return newlinks

print searchAP("cars")
