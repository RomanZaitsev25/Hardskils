# Разбор библиотеки BeautifulSoup

import re

from bs4 import BeautifulSoup

with open('afisha1.html') as file:
    src = file.read()
    # print(src)

soup = BeautifulSoup(src, 'lxml')
# title = soup.title
# print(title)
# print(title.text)
# FIND AND FIND_ALL
# page_h1 = soup.find_all('h1')
# for i in page_h1:
#     print(i.text)
# user_name = soup.find('div', class_='user__birth__date').find('span')
# # user_year = soup.find('div', class_="user__birth__date")
# print(user_name)

# нахождение элемента с помощью словаря
# user_spam = soup.find('div', class_='user__info').find_all('span')
# print(user_spam)
#
#
# for item in user_spam:
#     print(item.text)


# спарсить ссылки соц сетей пользователя.

# social_lincs = soup.find('div', class_='social__networks').find('ul').find_all('a')
# # print(social_lincs)
# for item in social_lincs:
#     print(item)

# all_a = soup.find_all('a')
# for item in all_a:
#     item_text = item.text
#     links = item.get('href')
#     print(f"{item_text}:{links}")

# find_parents(), find_parent()

# post_a = soup.find(class_='post__text').find_parent()
# print(post_a)

# post_a = soup.find(class_='post__text').find_parent('div',
#                                                     class_='user__post')
# print(post_a)


# post_a = soup.find(class_='post__text').find_parents()
# print(post_a)


#next_element .previous_elements
# a=soup.find('div', class_='post__title')
# print(a.text)

# a=soup.find('div', class_='post__title').next_element.next_element
# print(a.text)

# find_next_sibling and find_previous_sibling

# asd = soup.find(class_='post__title').find_next_sibling()
# print(asd)

# Получить ссылки
# sdsd = soup.find(class_='some__links').find_all('a')
# print(sdsd)
# for item in sdsd:
#     item_text = item.text
#     link = item.get('href')
#     link2 = item.get('data-attr')
#     print(f'{item_text}:{link}{link2}')

# Найти значение Одежда
# find_a_by_text = soup.find('a', text=re.compile('Closer'))
# print(find_a_by_text)

# find_all_by_text = soup.find_all(text=re.compile('[Cc]loser'))
# print(find_all_by_text)

