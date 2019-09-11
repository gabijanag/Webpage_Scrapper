'''
Use the BeautifulSoup and requests Python packages
to print out a list of all the article titles on the
BBC news page.
'''

import requests
from bs4 import BeautifulSoup

# load the nytimes HTML
r = requests.get('https://www.bbc.com/news')
soup = BeautifulSoup(r.content, 'lxml')

# get all the article titles
print(soup.find_all(class_="gs-c-promo-heading"))
