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
headings = soup.find_all(class_='gs-c-promo-heading__title')
print(headings)
headingslist =[]
for item in headings:
    headingslist.append(item.text)


print(len(headings)) #how many headings are there
print(len(headingslist)) #check how many scraped
print(headingslist)

# put all the items into a csv file
import numpy as np
np.savetxt("Scraper.csv", headingslist, delimiter=",", fmt='%s', header='Article Titles')

# in case you have multiple lists that need to be stacked
#
# np.savetxt("scraper.csv", np.column_stack((headingslist, \
# urllist)), delimiter=",", fmt='%s', header=header)