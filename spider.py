#coding:utf-8

import urllib2
import Queue
import re
import sys

from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')

global_links = []

host = 'http://www.shnu.edu.cn'

index = 0
def find_href(url):
    global index

    index +=1
    print url
    
    global_links.append(url)

    try:
        request = urllib2.Request(url)

        url_opener = urllib2.build_opener()

        response = url_opener.open(request,timeout=3)

        context = response.read()

        soup = BeautifulSoup(context, "html.parser")

        file_object = open('data/{0}.txt'.format(0), 'a')
        file_object.write('{0},{1}\n'.format(soup.title.string,url))
        file_object.close()

        links = []

        for link in soup.find_all('a', href=True):

            if link.get_text(strip=True):
                a = link['href']

                if 'http' not in a and 'javascript' not in a:
                    a = '{0}{1}'.format(host, a)

                if 'www.shnu.edu.cn' in a and '_upload' not in a:
                    links.append(a)

        for link in links:
            if link not in global_links:
                find_href(link)
                print link

    except KeyboardInterrupt:  
        sys.exit()
    except Exception,err:
        print  err


find_href(host)
