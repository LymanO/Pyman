import urllib2
import time
from bs4 import BeautifulSoup
import threading

global count
count = 0


def countpic():
    global count
    count = count +1


def downloadpic(urlend='3000/1',urlname='3000-1'):

    url = "http://img1.mm131.com/pic/%s.jpg" % urlend
    filename = urlend.replace('/','-') + urlname
    try:
        picurl = urllib2.urlopen(url)
        if picurl.getcode() == 200:
            pic = picurl.read()
            with open("PIC/%s.jpg" % filename, 'wb') as picfile:
                picfile.write(pic)
            countpic()
            print ("%d.download %s succeed!" %(count, filename))
            return True
    except urllib2.URLError:
        print ("----Download all this series.")
        return False


def downloadpicseris(sta,urlname=''):

    for i in range(1,100):
        urlend="%d/%d"%(sta,i)
        if not downloadpic(urlend,urlname):
            if i == 1:
                return False
            else:
                return True
            break
    pass


def get_series_name(startno):
    urls = 'http://m.mm131.com/xinggan/%d.html' % startno
    try:
        url_files = urllib2.urlopen(urls)
        response = url_files.read()
        soup = BeautifulSoup(response,'html.parser')
        name = soup.h2.string
        return name
    except urllib2.HTTPError:
        return 'mm'


if __name__ == '__main__':
    """
    Download the certain series pictures.
    """
    starttime = time.time()
    end = 3112
    start = 3110
    name = get_series_name(start)
    while downloadpicseris(start,name):
        start = start+1
        name = get_series_name(start)
        if start >= end:
            break
    endtime = time.time()
    print "Total %d pictures." % count
    print "Total spend %d seconds." % (endtime-starttime)