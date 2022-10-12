import requests
from bs4 import BeautifulSoup


def get_data(URL):
    headers = {

        "accept": "* / *",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 "
                      "Safari/537.36 OPR/90.0.4480.84", "X-Amzn-Trace-Id":
            "Root=1-6342bf0a-43cfba677d4ec8835339823a"
    }
    req = requests.get(URL, headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')

    html_text = soup.find_all('span', class_='result__name')
    html_price = soup.find_all('span', class_="g-price g-oldprice result__oldprice")

    new_inf = dict(zip(html_text, html_price))

    for key, item in new_inf.items():
        print(f'{key.text}:-{item.text}')

    with open('text.html', 'a+', encoding='utf-8') as file:
        for key, item in new_inf.items():
            file.write(f'{key.text}:- {item.text} \n')


single_req = requests.get("https://www.21vek.by/mobile/")

page = BeautifulSoup(single_req.text, "html.parser")

page_amount = page.findAll('a', class_='j-load_page cr-paging_link')

# print(page_amount)
page_amount = [item.text for item in page_amount]
# print(page_amount)
page_amount.remove('...')
page_amount.remove(">")
page_amount = [int(item) for item in page_amount]
max_page = max(page_amount)
# print(page_amount)

for page in range(1, max_page + 1):
    get_data(f'https://www.21vek.by/mobile/page:{page}/')
