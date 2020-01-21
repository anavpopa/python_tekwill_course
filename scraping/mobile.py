import csv
import json
import requests
from bs4 import BeautifulSoup

schema = 'https://999.md/ru/list/phone-and-communication/mobile-phones'
href = '?hide_duplicates=yes&view_type=detail'
pages = [schema + href]

page = requests.get(schema + href)
soup = BeautifulSoup(page.content, 'html.parser')
pagination = soup.find('nav', class_='paginator')
pages = pagination.find_all('li')
last_page = pagination.find('li', class_='is-last-page')
last_page_href = last_page.find('a')['href'][-3:]

pages = []
data = []
for i in range(int(last_page_href)):
    url = schema + href + '&page='+ str(i+1)
    print('fetching ', url)
    page = requests.get(url, stream=True)
    soup = BeautifulSoup(page.content, 'html.parser')
    mobiles = soup.find_all('li', class_='ads-list-detail-item')

    for mobile in mobiles:
        try:
            title = mobile.find('div', class_ = 'ads-list-detail-item-title').find('a').text
            price = mobile.find('div', class_ = 'ads-list-detail-item-price').text.replace('\xa0', ' ').strip()
            description = mobile.find('div', class_ = 'ads-list-detail-item-intro').text.replace('\n', ' ').strip()
        except AttributeError:
            print('Errors in ad')

        data.append({
            'title': title, 'price': price, 'description': description
        })
        # print({
        #     'title': title, 'price': price, 'description': description
        # })


with open('mobile.csv','w', newline = '', encoding = 'utf-8') as csv_file:
    keys = data[0].keys()
    dict_writer = csv.DictWriter(csv_file, fieldnames=keys)
    dict_writer.writeheader()
    dict_writer.writerows(data)

with open('mobile.json', 'w', newline = '', encoding = 'utf-8') as json_file:
    json.dump(data, json_file)