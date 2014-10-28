from bs4 import BeautifulSoup
import csv
import urllib2

with open('artistsAndLinks.csv', 'wb') as csvfile:
    fileWriter = csv.writer(csvfile)
    fileWriter.writerow(['Name', 'Link URL'])
    for x in range(97, 123):
        pageFile = urllib2.urlopen("http://www.sing365.com/artist/"+str(unichr(x))+".html")

        pageHtml = pageFile.read()

        pageFile.close()

        soup= BeautifulSoup(pageHtml,"lxml")
        sAll = soup.findAll('a')

        name = ""
        linkurl = ""

        for a in sAll:
            if len(a.string.encode('utf-8'))>7:
                name = a.string.encode('utf-8')[:-7]
            if len(a.attrs['href'].encode('utf-8'))>25:
                linkurl = "http://www.sing365.com"
                linkurl += str(a.attrs['href'].encode('utf-8'))
            if(name != "" and linkurl != ""):
                fileWriter.writerow([name] + [linkurl])
