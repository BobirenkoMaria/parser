import requests
from bs4 import BeautifulSoup

info = []

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/100.0.4896.127 Safari/537.36 OPR/86.0.4363.64', 'accept': '*/*'}


def get_html(url, params=None):
    try:
        r = requests.get(url, headers=HEADERS, params=params)
    except requests.exceptions.ConnectionError:
        return None
    return r


def get_url(articul, url, website):
    if website == 1:
        url = 'https://wasserkraft.ru/search-results?query=' + str(articul)

    elif website == 2:
        url = 'https://davitamebel.ru/search/?q=' + str(articul).replace("{", "").replace("}", "").replace("'", "")
    return url


def items_are_empty(website):
    if website == 1:
        info.append({
            'title': '',
            'main_photo': '',
            'photos': '',
            'price': '0',
            'dimensions': '',
            'material': '',
            'gross weight': ''
        })
    elif website == 2:
        info.append({
            'title': '',
            'price': '0',
            'material': '',
            'collection': '',
            'description': ''
        })


def get_product_item(product_items, product):
    for item in product_items:
        item = item.get_text()
        item = " ".join(item.split())
        try:
            if item.split()[0] == product:
                return item
        except IndexError:
            pass
    return ''


def get_content(html, website, articul):
    soup = BeautifulSoup(html, 'html.parser')
    items = ''
    href_now = ''

    if website == 1:
        items = soup.find_all('a', itemprop='name', href=True)
        articul = str(articul).replace("{", "").replace("}", "").replace("'", "")

        item_i = 0
        needed_articul = False
        while not needed_articul:
            if len(items) != 0:
                item_articul = (items[item_i].get_text()).split()[1]

                if articul == item_articul:
                    href_now = 'https://wasserkraft.ru/' + items[item_i].get('href')
                    website_parse(href_now, website)
                    needed_articul = True
                else:
                    item_i += 1
            elif len(items)-1 == item_i:
                items_are_empty(website)
                needed_articul = True
            else:
                items_are_empty(website)
                needed_articul = True

    elif website == 2:
        items = soup.find('a', target='_self', itemprop='name', href=True)
        if items is not None:
            item = soup.find('strong')
            item_articul = (item.get_text()).split()[1]
            articul = str(articul).replace("{", "").replace("}", "").replace("'", "")
            if item_articul == articul:
                href_now = 'https://davitamebel.ru' + items.get('href')

                website_parse(href_now, website)
            else:
                items_are_empty(website)

    if items == None:
        items_are_empty(website)


def get_website_content(html, website):
    soup = BeautifulSoup(html, 'html.parser')

    if website == 1:
        title = soup.find('h1', class_="catalog-header__title title")
        main_photo = soup.find('a', class_="product-carousel__item zoom", href=True)
        photos = soup.find_all('a', class_='product-carousel__item zoom', href=True)
        price = soup.find('span', itemprop="price")

        product_items = soup.find_all('div', class_='product__item')
        dimensions = get_product_item(product_items, 'Размер')
        material = soup.find('div', class_='product__item not_list')
        gross_weight = get_product_item(product_items, 'Вес')


        info.append({
            'title': title.get_text(),
            'main_photo': 'https://wasserkraft.ru/' + str(main_photo.get('href')),
            'photos': getList(photos, website),
            'price': price.get_text(),
            'dimensions': dimensions[7:-2],
            'material': (str(material.get_text()).strip())[9:],
            'gross weight': gross_weight[12:]
        })
    elif website == 2:
        title = soup.find('h1', itemprop="name")
        price = soup.find('span', class_="old-price hidden-xs")
        if (price == None):
            price = soup.find('span', itemprop="price")

        materials = soup.find('div', class_='product-info')
        materials = materials.find_all('li')
        materials = getList(materials, website)

        collection = title.find('strong')
        description = soup.find('div', itemprop='description')


        info.append({
            'title': title.get_text(),
            'price': (price.get_text()).replace('\xa0', '')[:-2],
            'material': materials,
            'collection': ((collection.get_text()).split(' '))[0],
            'description': description.get_text()
        })



def getList(tegs, website):
    str_list = []

    if website == 1:

        for teg in tegs:
                str_list.append('https://wasserkraft.ru/' + str(teg.get('href')))

        str_list.pop(0)

        index = 0
        for tag in str_list:
            if tag.find(' black.jpg') != -1:
                index = str_list.index(tag)
                str_list.remove(str_list[index])

    elif website == 2:
        for teg in tegs:
            str_list.append(teg.get_text())

    str_list = '; '.join(str_list)

    return str_list


def parse(articuls, start_line, count, website):
    count -= start_line
    start_line1 = start_line

    URL = ''

    i=1
    for articul in articuls:
        URL = get_url(articul, URL, website)

        html = None
        while html == None:
            html = get_html(URL)
            try:
                if html.status_code == 200:
                    get_content(html.text, website, articul)
                    start_line1 += 1

                    print(str(round(i*100/count)) + '%')
                    i+=1

            except AttributeError:
                print("Connetction refused")

    return info


def website_parse(url, website):
    html = None
    while html == None:
        html = get_html(url)
        try:
            if html.status_code == 200:
                get_website_content(html.text, website)
        except AttributeError:
            print("Connection refused in website_parse")
