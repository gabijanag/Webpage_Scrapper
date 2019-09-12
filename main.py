'''
Use the BeautifulSoup and requests Python packages
to print out a list of all the article titles on the
BBC news page.
'''

import requests
from bs4 import BeautifulSoup

# load the HTML
r = requests.get('https://www.bbc.com/news')
soup = BeautifulSoup(r.content, 'lxml')

# get all the article titles
headings = soup.find_all(class_='gs-c-promo-heading')
print(headings)
headingslist =[]
for item in headings:
    headingslist.append(item.text)

# print(len(headings)) #how many headings are there
print(len(headingslist)) #check how many scraped


# get all the URL corresponding to the article titles
urls = []
for url in headings:
    urls.append(url.get('href'))

print(urls)
print(len(urls))


# put all the items into a csv file
import numpy as np
headers = 'Article Titles' 'Urls'
np.savetxt("scraper.csv", np.column_stack((headingslist, \
urls)), delimiter=" | ", fmt='%s', header='Article Title | URL')