#!/usr/bin/python3
import urllib
import urllib.request
from bs4 import BeautifulSoup

def main() :
        uri = "http://www.distrowatch.com/"
        page = urllib.request.urlopen(uri)
        soup = BeautifulSoup(page , "html.parser")
        rank = 1
        for link in soup.findAll("tr") : 
                for data in link.findAll("td" , {"class" : "phr2"}):
                        print("{}.".format(rank).ljust(4) , end = "\t ")
                        print(data.text.ljust(20) , end = "\t ")
                        rank = rank + 1
                for data in link.findAll("td" , {"class" : "phr3"}):
                        print(data.text)
if __name__ == "__main__" : main()
