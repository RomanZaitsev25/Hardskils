# Дан get запрос, распарсить его и достать строку This is page и записать
# его в новый текстовый файл.

import requests

URL = 'https://w3schools.com/python/demopage.htm'
try:
    response = requests.get(URL)
except Exception as a:
    print(a)
else:
    text = ''
    format_text = response.text.split('\n')
    print(format_text)
    for item in format_text:
        if '<h1>This is a Test Page</h1>' in item:
            text = item
    print(text)
    text = text.replace('<h1>', '')
    text = text.replace('</h1>', '')
    print(text)

with open('text_3.txt', 'w') as file:
    file.write(text)
