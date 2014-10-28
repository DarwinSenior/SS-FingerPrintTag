from bs4 import BeautifulSoup

import urllib2
names=open("artistList.txt", "w")
for x in range(97, 123):
    pageFile = urllib2.urlopen("http://www.sing365.com/artist/"+str(unichr(x))+".html")

    pageHtml = pageFile.read()

    pageFile.close()

    soup= BeautifulSoup(pageHtml,"lxml")
    sAll = soup.findAll('a')

    for a in sAll:
        if len(a.string.encode('utf-8'))>7:
            name = a.string.encode('utf-8')[:-7]
            names.write(name + "\n")

names.close()