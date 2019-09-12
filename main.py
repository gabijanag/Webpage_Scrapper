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
# headings = soup.find_all('h3')
headings = soup.find_all(class_='gs-c-promo-heading__title')
print(headings)
headingslist =[]
for item in headings:
    headingslist.append(item.text)


print(len(headings)) #how many headings are there
print(len(headingslist)) #check how many scraped
print(headingslist)
