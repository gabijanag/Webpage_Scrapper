# Simple Python Webpage Scrapper

This Scrapper gets the article titles and URL's from the BBC news webpage.

It fetches data from the website and saves it into a .csv file.

## Installation

* ```git clone``` this repo

* ```cd Scrapper```

* ```pip install -r requirements.txt```

* ```python main.py```

## Usage

The scraper is implemented as a Python 3 script in ```main.py```. 
Fill in URL of the webpage you want to scrape at the beginning of the file. 
Then run the script by cd into the directory containing the script, running python3 main.py.


###### Third party Packages
* Python Requests: http://docs.python-requests.org/en/master/
```
pip install requests
```
This loads the webpage's HTML

* BeautifulSoup 4: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
```
pip install beautifulsoup4
```
This allows to search & extract content from the HTML 
