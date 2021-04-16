from requests_html import HTMLSession
import requests
import pandas as pd
from bs4 import BeautifulSoup
from dateutil.parser import parse
import matplotlib.pyplot as plt
import csv

class Scraper:

    def __init__(self,baseurl):
        self.baseurl = baseurl
        pass

    def getUrls(self):
        #baseurl ="https://www.goodreads.com/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
        }
        self.url_links= []
        for x in range(1):
            r = requests.get(f"https://www.goodreads.com/list/show/264.Books_That_Everyone_Should_Read_At_Least_Once?page={x}")
            soup = BeautifulSoup(r.content, 'lxml')
            book_pages = soup.find_all('tr', {'itemtype':'http://schema.org/Book'})
            for item in book_pages:
                link = item.find('a',{'itemprop':'url'})['href']         
                self.url_links.append(self.baseurl + link)
            print(len(self.url_links))
        print(self.url_links)
        return self.url_links
        
    
                

    def BooksInfo(self):
        for links in self.url_links[0:1]:
            s = HTMLSession()
            r = s.get(links)
            r.html.render(timeout = 40)

            self.book = {
                "title":r.html.xpath('//*[@id="bookTitle"]',first=True).text, 
                'authors': r.html.xpath('//*[@id="bookAuthors"]/span[2]/div/a/span',first=True).text,
                'reviews': r.html.xpath('//*[@id="bookMeta"]/a[3]',first=True).text,
                'ratings': r.html.xpath('//*[@id="bookMeta"]/a[2]',first=True).text,
                'avg_rating': r.html.xpath('//*[@id="bookMeta"]/span[2]',first=True).text,
                'num_pages': r.html.xpath('//*[@id="details"]/div[1]/span[2]',first=True).text,
                'original_publish_year': r.html.xpath('//*[@id="details"]/div[2]/nobr',first=True).text,
                'series': r.html.xpath('//*[@id="bookDataBox"]/div[3]/div[2]/a',first=True).text,
                #'genre':r.html.xpath('/html/body/div[2]/div[3]/div[1]/div[2]/div[3]/div[6]/div/div[2]/div/div[1]/div[1]/a',first=True).text,
                'awards': r.html.xpath('//*[@id="bookDataBox"]/div[7]/div[2]',first=True).text,
                
                
                }
            return self.book

    def write_csv(self):
        with open('books.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow([self.book['title'],self.book['authors'],self.book['reviews'],self.book['ratings'],self.book['avg_rating'],self.book['num_pages']
            ,self.book['original_publish_year'],self.book['series'],self.book['awards']])
        
            


test = Scraper("https://www.goodreads.com/")
test.getUrls()
test.BooksInfo()
test.write_csv()
