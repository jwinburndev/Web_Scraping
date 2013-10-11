import nltk
import urllib
import urlparse
from bs4 import BeautifulSoup
from readability.readability import Document
from readability.readability import Document
import mechanize
import datetime
import MySQLdb


br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Firefox')]

def insertDB(resp):
    host = "mysql.youtube.com"
    user = "youtubeadmin"
    password = "youtubepass"
    conn = MySQLdb.connect(host=host, user = user, passwd = password, db="adbspider")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO scraped_articles (text,title,date,author,url,picture_url) VALUES (%s,%s,%s,%s,%s,%s)",(resp[0],resp[1],resp[2],resp[3],resp[4],resp[5]))
        data = cursor.fetchall()
        cursor.close()
        conn.close()

        conn = MySQLdb.connect(host=host, user = user, passwd = password, db="adbspider")
        cursor = conn.cursor()
        cursor.execute ("UPDATE scraped_articles SET paraphrase_flag = 1 WHERE url = %s",(resp[4]))
        data = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print "error inserting in to DB"




def getReadableArticle(url):

        now = datetime.datetime.now()
        resp = ["","","","","",""]
        images = []
        html = br.open(url).read()

        readable_article = Document(html).summary()
        #print readable_article
        #print readable_article
        readable_title = Document(html).title()
        #print readable_title
        soup = BeautifulSoup(readable_article)
        final_article = soup.text
        #print final_article
        #print final_article
        links = soup.findAll('img', src=True)
        for lin in links:
                li = urlparse.urljoin(url,lin['src'])
                #print li
                images.append( li)
                
        resp[0] = str(final_article.encode("ascii","ignore"))
        #print resp[0]
        resp[1] = str(readable_title.encode("ascii","ignore"))
        resp[2] = str(now.month)+" "+str(now.day)+" "+str(now.year)+"-"+str(now.hour)+":"+str(now.minute)+":"+str(now.second)
        resp[3] = url
        resp[4] = url
        #if len(images)>0:
                #resp[5] = images[0]
        #else:
        resp[5] = ""
        insertDB(resp)
        print "inserted resp"
                 

        title_article = []
        title_article.append(final_article)
        title_article.append(readable_title)
        title_article.append(images)                
        return title_article


	
print getReadableArticle("http://whitehouse.gov")
