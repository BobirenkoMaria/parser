import requests
from bs4 import BeautifulSoup


HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/100.0.4896.127 Safari/537.36 OPR/86.0.4363.64', 'accept': '*/*'}

def get_html(url, params=None):
    try:
        r = requests.get(url, headers=HEADERS, params=params)
    except requests.exceptions.ConnectionError:
        return None
    return r


def get_url(articul, url):
    url = 'https://wasserkraft.ru/search-results?query=' + str(articul)
    return url


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find('a', itemprop='name', href=True)

    href_now = 'https://wasserkraft.ru/' + items.get('href')
    website_parse(href_now)


def get_website_content(html):
    info = []

    soup = BeautifulSoup(html, 'html.parser')

    title = soup.find('h1', class_="catalog-header__title title")
    main_photo = soup.find('a', class_="product-carousel__item zoom", href=True)
    photos = soup.find_all('a', class_='product-carousel__item zoom', href=True)
    price = soup.find('span', itemprop="price")



    print(photos)

    info.append({
        'title': title.get_text(),
        'main_photo': 'https://wasserkraft.ru/' + str(main_photo.get('href')),
        'price': price.get_text()
    })

    print(info)


def parse(articuls):
    URL = ''

    for articul in articuls:
        URL = get_url(articul, URL)

        html = None
        while html == None:
            html = get_html(URL)
            try:
                if html.status_code == 200:
                    get_content(html.text)

            except AttributeError:
                print("Connection refused")


def website_parse(url):
    html = None
    while html == None:
        html = get_html(url)
        try:
            if html.status_code == 200:
                #print(html.text)

                get_website_content(html.text)
        except AttributeError:
            print("Connection refused in website_parse")
