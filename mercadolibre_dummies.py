from bs4 import BeautifulSoup
from requests import get

url = 'https://carros.mercadolibre.com.co/carros_Desde_49_NoIndex_True'

def getHtml(url):
    response = get(url)
    return response.text

def get_soup(html):
    return BeautifulSoup(html, 'html.parser')

def get_link(page):
    link = page.select_one('li.andes-pagination__button--next > a')
    return link['href']


for current_page in range(1, 10):
    page = get_soup(getHtml(url))
    for card in page.select('li.ui-search-layout__item'):
        title = card.select_one('div > div.ui-search-item__group--title > h2').string
        price = card.select_one('span.price-tag-fraction').string
        print(title, price)
    url = get_link(page)