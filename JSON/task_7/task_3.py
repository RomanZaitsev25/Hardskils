#  Спарсить данный название телефона и стоимость его, сохраанить  страницу
#  в zip файл, и затем zip файл распарсить
import requests
from bs4 import BeautifulSoup
import zipfile


def get_data(URL, page_number):
    headers = {
        "accept": "* / *",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 "
                      "Safari/537.36 OPR/90.0.4480.84",
        "X-Amzn-Trace-Id": "Root=1-6342bf0a-43cfba677d4ec8835339823a"
    }
    req = requests.get(URL, headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')

    html_items = soup.find_all('li', class_='result__item')
    new_inf = []


    for item in html_items:
        html_name = item.find('span', class_="result__name").text
        if item.find('span', class_="g-item-data") is None:
            html_price = ""

        else:
            html_price = item.find('span', class_="g-item-data").text

        new_inf.append((html_name, html_price))

    print(new_inf)

    count = 1
    for item in new_inf:
        print(f'{count}.{item[0]}:-{item[1]}')
        count += 1

    with open(f'text-page-{page_number}.html', 'w', encoding='utf-8') as file:
        for item in new_inf:
            file.write(f'{item[0]}:-{item[1]}\n')


single_req = requests.get("https://www.21vek.by/mobile/")

page = BeautifulSoup(single_req.text, "html.parser")

page_amount = page.findAll('a', class_='j-load_page cr-paging_link')

page_amount = [item.text for item in page_amount]
page_amount.remove('...')
page_amount.remove(">")
page_amount = [int(item) for item in page_amount]
max_page = max(page_amount)

for page in range(1, max_page + 1):
    get_data(f'https://www.21vek.by/mobile/page:{page}/', page)


with zipfile.ZipFile('full_text.zip', 'w') as archive:
    for page in range(1, max_page + 1):
        archive.write(f'text-page-{page}.html')

with zipfile.ZipFile('full_text.zip', 'r') as archive:
    archive.extractall("./")
