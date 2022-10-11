# C сайта спарсить все названия объявлений и цены и отправить в отдельный файл
import requests
from bs4 import BeautifulSoup


def new_ads(URL):
    headers = {

        "accept": "* / *",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 "
                      "Safari/537.36 OPR/90.0.4480.84", "X-Amzn-Trace-Id":
            "Root=1-6342bf0a-43cfba677d4ec8835339823a"
    }
    response = requests.get(URL, headers=headers)
    # print(response.text)

    soup = BeautifulSoup(response.text, 'html.parser')

    itemName = soup.find_all('h3', class_='styles_title__wj__Y')
    itemPrice = soup.find_all('p', class_='styles_price__x_wGw')
    # print(itemName)
    # print(itemPrice)

    new_list = []
    for item in itemPrice:
        new_list.append(item.text)
    # print(new_list)

    new_list2 = []
    for item2 in itemName:
        new_list2.append(item2.text)
    # print(new_list2)

    a = dict(zip(new_list2, new_list))
    # print(a)

    for key, item in a.items():
        print(key, '-', item)

    with open('text.html', 'w', encoding='utf-8') as file:
        for key, item in a.items():
            file.write(f'{key}:-, {item}\n')


new_ads('https://www.kufar.by/l')


