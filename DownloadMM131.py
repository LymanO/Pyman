# coding ='utf-8'

from bs4 import BeautifulSoup
import urllib2
import os
import time

import DownloadPics


def download_series(series_no,series_name):
    startno = int(series_no)
    return DownloadPics.downloadpicseris(startno,series_name)
    pass

def existing_series():
    listname = []
    for root, dirs, files in os.walk("PIC", topdown=False):
        files = list(set(files))
        for name in files:  # usually the filename like 3000-text-No.jpg
            if name[-3:].lower() == 'jpg':  # check if the format is jpg or not
                naNo = name[:4]
                listname.append(naNo)
    # listname.sort()
    listname = list(set(listname))  # remove the duplicated numbers
    print 'Already download %d series:' % len(listname)
    listname.sort(reverse=True)
    print listname
    # print '-------'
    return listname


def download_new():
    url = "http://m.mm131.com/"
    url_file = urllib2.urlopen(url)
    response = url_file.read()
    soup = BeautifulSoup(response, 'html.parser')
    links = soup.content.find_all('a', attrs={'class': "post-title-link"})
    alreadyDownloadPics = existing_series()
    newPics = []
    print 'front page series:'
    for link in links:
        urlname = link.string
        urlSeries = link.get('href')
        new_series = urlSeries[-9:-5]  # get the series no
        print new_series
        if new_series not in alreadyDownloadPics:
            newPics.append(new_series)
            download_series(new_series,urlname)
    print 'new series: %d' % newPics.count()



if __name__ == "__main__":
    #downloadType = input('Type 1 to download new series, Type 2 to download certain series:')
    #if downloadType == '1':
    start = time.time()
    download_new()
    end = time.time()
    print "--total spend time %ds--" % int(end - start)
    #else:
