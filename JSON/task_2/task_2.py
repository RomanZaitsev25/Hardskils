import requests

# params = {'q': 'Лондон', 'appid': API_Token, 'units': 'metric'}
# response = requests.get('https://api.openweathermap.org/data/2.5/weather',
#                         params=params)


# response = requests.get('https://jsonplaceholder.typicode.com/posts')
# x = response.json()
# print(type(x))
# new_list = []
# i = 0
# for until in x:
#     if until['id'] >= 5:
#         new_list.append(until)
#     i += 1
# print(new_list)
# print(response.headers)
# print(response.status_code)
# print(response.content)
# print(response.text)
# print(response.json())

#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84",
# }
#
# URL = 'https://www.kinopoisk.ru/lists/movies/top250/'
# response = requests.get(URL, headers=headers)
#
# print(response.text)


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84",
}

data = {'custname': 'login', 'custtel': 84551212, 'custemail': 'roman@tut.by',
        'size': 'medium', 'topping': 'bacon', 'delivery': 'comments:'}
URL = 'https://httpbin.org/post'
# Должны быть куки, но нам не нужно о них забоиться, т.к. они сохранятся
# в сесии. поэтому для гед запроса. Нам нужно найти токен передать словарик,
# и написать его в Post запрос. Если при переходе на другую страницу, меняется
# адрессб нам нуэно в пост запрос добавить
variable = requests.session()
aa = variable.get('https://httpbin.org/form/post')
response = variable.post(URL, headers=headers, data=data, allow_redirects=True)
print(type(response.text))
x = response.json()
print(x)
s = x['form']['custname']
print(s)
