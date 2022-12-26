import json
import time
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pickle


with open('yandex.json', 'r', encoding='utf-8') as file:
    json_text = file.read()
    read = json.loads(json_text)
    LOGIN = read['LOGINS']
    password = read['PASSWORD']

options = webdriver.ChromeOptions()

options.add_argument(
    'User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84,'
    ' X-Amzn-Trace-IdRoot=1-6342bf0a-43cfba677d4ec8835339823a')



driver = webdriver.Chrome(
    executable_path='C://Users//Роман//PycharmProjects//Hardskils//Selenium//'
                    'chromdriver//chromedriver.exe',
    options=options)

URL = 'https://mail.yandex.ru/'
# URL = 'https://passport.yandex.ru/auth?retpath=https%3A%2F%2Fmail.yandex.ru%2F&backpath=https%3A%2F%2Fmail.yandex.ru%2F%3Fnoretpath%3D1&from=mail&origin=hostroot_homer_auth_ru'
try:
    driver.get(URL)
    time.sleep(5)
    enter_input = driver.find_element(by='tag name', value="button")
    # enter_input = driver.find_element(by='class name', value='PSHeader-Right')
    # enter_input = driver.find_element(by='class name', value='Button2-Text')
    enter_input.click()
    login_input = driver.find_element(by='name', value='login')
    login_input.clear()
    login_input.send_keys(LOGIN)
    login_input.send_keys(Keys.ENTER)
    time.sleep(5)
    password_input = driver.find_element(by='name', value="passwd")
    password_input.send_keys(password)
    time.sleep(5)
    password_input.send_keys(Keys.ENTER)
    time.sleep(5)
    login_input.send_keys(Keys.ENTER)
    pickle.dump(driver.get_cookies(), open(f'{LOGIN}_cookies', 'wb'))
    # driver.get(URL)
    # time.sleep(5)
    # for cookies in pickle.load(open(f'{login}_cookies', 'rb')):
    #     driver.add_cookie(cookies)
    # driver.refresh()
    # time.sleep()

except Exception as ex:
    print(ex)
else:
    driver.close()
    driver.quit()