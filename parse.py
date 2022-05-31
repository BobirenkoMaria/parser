import requests
from bs4 import BeautifulSoup


HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/100.0.4896.127 Safari/537.36 OPR/86.0.4363.64', 'accept': '*/*'}

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_url(articul, url):
    url = 'https://wasserkraft.ru/search-results?query=' + str(articul)
    return url


def get_content(html):
    href_now = ''

    soup = BeautifulSoup(html, 'html.parser')

    #try:
    items = soup.find('a', itemprop='name', href=True)
    #except requests.exceptions.ConnectionError:
        #items = soup.find('a', class_="product-card__figure", href=True)

    href_now = 'https://wasserkraft.ru/' + items.get('href')

    print(href_now)

    #website_parse(href_now)


def get_website_content(html):
    info = []

    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('h1', class_="catalog-header__title title")
    #price = soup.find('span', itemprop="price")
    #main_photo = soup.find('a', class_="product-carousel__item zoom slick-slide slick-current slick-active", href=True)

    info.append({
        'title': title.get_text(),
        #'main_photo': main_photo.get('href'),
        #'price': price.get_text()
    })

    print(info)


def parse(articuls):
    URL = ''
    for articul in articuls:
        URL = get_url(articul, URL)

        html = get_html(URL)
        if html.status_code == 200:
            get_content(html.text)
        else:
            print('error parse')


def website_parse(url):
    html = get_html(url)
    if html.status_code == 200:
        get_website_content(html.text)
    else:
        print('error website parse')
