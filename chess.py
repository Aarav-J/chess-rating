from webbrowser import get
from selenium import webdriver

import time 
import pyautogui


option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.add_argument("--headless")
option.add_argument("disable-gpu")
browser = webdriver.Chrome(executable_path='D:\GoogleChromeDriver\chromedriver.exe', options=option)
option.add_experimental_option("excludeSwitches", ['enable-automation']);

# browser.get("https://chess.com/member/poo1712")
user = input("chess username: ")

# for i in range(len(div)): 
#     print(div[i].text[0:-1])

while True:
    browser.get("https://chess.com/member/" + user)

    time.sleep(5)

    div = browser.find_elements_by_xpath('.//div[@class ="stat-section-section-header"]')

    for i in range(len(div)):
        header = div[i].find_element_by_class_name('stat-section-section-link-name')
        st = header.text

        if st == 'Blitz':
            rating = div[i].find_element_by_class_name('stat-section-user-rating').text
            print(rating)
            break
    for i in range(420):
        time.sleep(1)
        print(i)
print("done")