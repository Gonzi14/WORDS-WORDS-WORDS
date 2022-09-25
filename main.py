from english_words import english_words_set
import random
import requests
from bs4 import BeautifulSoup

theList = list(english_words_set)
print (theList[random.randrange(len(theList))])
URL = f"https://www.merriam-webster.com/dictionary/{theList[random.randrange(len(theList))]}"
page = requests.get(URL)
soup = BeautifulSoup(page.text, 'lxml')
box = soup.find('div', id = 'dictionary-entry-1')
definition = box.find('span').get_text()
print(definition)