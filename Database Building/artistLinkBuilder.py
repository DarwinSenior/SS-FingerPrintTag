from bs4 import BeautifulSoup

import urllib2
links=open("artistLinkList.txt", "w")
for x in range(97, 123):
    pageFile = urllib2.urlopen("http://www.sing365.com/artist/"+str(unichr(x))+".html")

    pageHtml = pageFile.read()

    pageFile.close()

    soup= BeautifulSoup(pageHtml,"lxml")

    sAll = soup.findAll('a')

    for a in sAll:
        if len(a.attrs['href'].encode('utf-8'))>25:
            st = "http://www.sing365.com"
            st += str(a.attrs['href'].encode('utf-8'))
            links.write(st + "\n")
links.close()