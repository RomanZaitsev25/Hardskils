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
    response = requests.get(URL, headers=headers)
    # print(response.text)

    soup = BeautifulSoup(response.text, 'html.parser')
    soup = soup.find_all('a', class_="movieItem_title")
    # print(soup)
    new_list = []
    for item in soup:
        new_list.append(item.text)
    print(new_list)

    with open('afisha.html', 'w', encoding='utf-8') as file:
        for item in new_list:
            file.write(item + '\n')


get_data('https://www.kinoafisha.info/rating/movies/')
