from selenium import webdriver
import time
import random




options = webdriver.ChromeOptions()
# options.add_argument('user-agent=My name Roman')
# options.add_argument(f'user-agent={random.choice(user_agents_list)}')
# options.add_argument(f'user-agent={useragent.opera}')

# set proxy
# options.add_argument("--proxy-server=37.215.59.11:8000")

proxy_options = {
    "proxy": {
        "https": f"http://{login}:{password}@37.215.59.11:8000"
    }
}

# driver = webdriver.Chrome(
#     executable_path="C:\\Users\\Роман\\PycharmProjects\\Hardskils\\"
#                     "Selenium\\chromdriver\\chromedriver.exe",
#     options=options
# )
driver = webdriver.Chrome(
    executable_path="C:\\Users\\Роман\\PycharmProjects\\Hardskils\\"
                    "Selenium\\chromdriver\\chromedriver.exe",
    seleniumwire_options=proxy_options
)

# "C:\\users\\selenium_python\\chromedriver\\chromedriver.exe"
# r"C:\users\selenium_python\chromedriver\chromedriver.exe"

url = "https://www.instagram.com/"
try:
    # driver.get(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent")
# time.sleep(5)
# driver.get(url="https://stackoverflow.com/")
# time.sleep(5)

# driver.refresh()
# driver.get_screenshot_as_file("1.png")
# driver.get(url="https://stackoverflow.com/")
# time.sleep(5)
# driver.save_screenshot("2.png")
# time.sleep(2)
    driver.get(url="https://2ip.ru")
    time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
