#  Спарсить данный название телефона и стоимость его, сохраанить каждую страницу
#  в отдельный файл, и затем каждый файл превратить в zip файл
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

# ДЗ: сделать запись всех файлов в отдельный архив
with zipfile.ZipFile('text1.zip', 'w') as archive:
    archive.write('text-page-1.html')

with zipfile.ZipFile('text2.zip', 'w') as archive:
    archive.write('text-page-2.html')

with zipfile.ZipFile('text3.zip', 'w') as archive:
    archive.write('text-page-3.html')

with zipfile.ZipFile('text4.zip', 'w') as archive:
    archive.write('text-page-4.html')

with zipfile.ZipFile('text5.zip', 'w') as archive:
    archive.write('text-page-5.html')

with zipfile.ZipFile('text6.zip', 'w') as archive:
    archive.write('text-page-6.html')

with zipfile.ZipFile('text7.zip', 'w') as archive:
    archive.write('text-page-7.html')

with zipfile.ZipFile('text8.zip', 'w') as archive:
    archive.write('text-page-8.html')

with zipfile.ZipFile('text9.zip', 'w') as archive:
    archive.write('text-page-9.html')

with zipfile.ZipFile('text10.zip', 'w') as archive:
    archive.write('text-page-10.html')

with zipfile.ZipFile('text11.zip', 'w') as archive:
    archive.write('text-page-11.html')

with zipfile.ZipFile('text12.zip', 'w') as archive:
    archive.write('text-page-12.html')

with zipfile.ZipFile('text13.zip', 'w') as archive:
    archive.write('text-page-13.html')

with zipfile.ZipFile('text14.zip', 'w') as archive:
    archive.write('text-page-14.html')

with zipfile.ZipFile('text15.zip', 'w') as archive:
    archive.write('text-page-15.html')