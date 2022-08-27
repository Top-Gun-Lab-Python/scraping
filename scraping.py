from bs4 import BeautifulSoup
from requests import get
 
html = get('https://quotes.toscrape.com/page/1/').text
 
soup = BeautifulSoup(html, 'html.parser')

listOfCards = []
for quote in soup.find_all('div', class_='quote'):
    title = quote.find('span', class_='text').get_text()
    author = quote.find('small', class_='author').get_text()
    listOfCards.append({'title': title, 'author': author, 'tags': []})

print(listOfCards)