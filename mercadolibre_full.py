from requests import get
from bs4 import BeautifulSoup as soup

class ProductsParser:
    def __init__(self, card, schema):
        self.card = card
        self.schema = schema

    def parse(self):
        return { 'title': self.getTitle(),'price':self.getPrice()}

    def getTitle(self):
        
        try:
            title = self.card.select_one(self.schema['title'])
            
            return title.get_text()
        except:
            return None

    def getPrice(self):
        try:
            price = self.card.select_one(self.schema['price'])
            return price.string
        except:
            return None


def getHtml(url):
    response = get(url)
    return response.text

def getNext(parser, schema):
    
    next = parser.select_one(schema['next'])
    return next['href']

def getParser(html):
    return soup(html, 'html.parser')

def getProducts(parser, schema):
    return parser.select(schema['discriminator'])

def scrap(schema):
    html = getHtml(schema['url'])
    for i in range(1,10):
        parser = getParser(html)
        for tree in getProducts(parser, schema):
            productsParser = ProductsParser(tree, schema)
            print(productsParser.parse())
        html = getHtml(getNext(parser, schema))

mercadolibre = {
    'url': 'https://carros.mercadolibre.com.co/carros_Desde_49_NoIndex_True',
    'discriminator': 'li.ui-search-layout__item',
    'title': 'div.ui-search-item__group--title > h2',
    'price' : 'span.price-tag-fraction',
    'next':'ul > li.andes-pagination__button--next > a'
}
scrap(mercadolibre)