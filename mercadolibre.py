from requests import get
from bs4 import BeautifulSoup as soup

class ProductsParser:
    def __init__(self, tree, schema):
        self.tree = tree
        self.schema = schema

    def parse(self):
        return { 'title': self.getTitle(),'img':self.getImg(),'price':self.getPrice()}

    def getTitle(self):
        
        try:
            title = self.tree.select_one(self.schema['title'])
            return title.string
        except:
            return None

    
    def getImg(self):
        try:
            img = self.tree.select_one(self.schema['img'])
            return img['title']
        except:
            return None

    def getPrice(self):
        try:
            price = self.tree.select_one(self.schema['price'])
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
    'url': 'https://computacion.mercadolibre.com.co/portatiles/_Desde_101',
    'discriminator': 'li.results-item',
    'title': 'div > h2 > a > span',
    'price' : 'span.price__fraction ',
    'img':'div > div > a > img',
    'next':'ul > li.andes-pagination__button.andes-pagination__button--next > a'
}
scrap(mercadolibre)