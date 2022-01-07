from bs4 import BeautifulSoup
import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import telebot


token = 'ваш токен'
bot = telebot.TeleBot(token)
while True:
    options = webdriver.ChromeOptions()
    s=Service(r'C:\Users\shiro\PycharmProjects\test\chromedriver.exe')
    driver = webdriver.Chrome(service=s, options=options)
    url='https://wax.atomichub.io/market?collection_name=spaceheroes1&order=asc&schema_name=heroes&sort=price&symbol=WAX'
    driver.get(url)

    sleep(5)

    src = driver.page_source
    with open("index.html", "w", encoding='utf-8') as file:
        file.write(src)

    with open("index.html",encoding='utf-8') as file:
         src = file.read()

    all_dict ={}

    soup = BeautifulSoup(src, "lxml")
    prices= soup.find_all(class_='price-color')
    hrefs = soup.find_all(class_='picture-position')
    all_nft = soup.find_all(class_= 'MarketCard large-card')
    prices_list=[]
    href_list= []


    for item in prices:
        item_text = item.text
        prices_list.append(item_text)
        # print(item.text)

    for href in hrefs:
        item_href =f'https://wax.atomichub.io' + href.get("href")
        href_list.append(item_href)
        # print(item_href)

    for i in range(len(prices_list)):
        all_dict [prices_list[i]] = href_list[i]

    with open("all_categories_dict.json") as file:
        all_load = json.load(file)

    price_cur= all_load.keys()
    price_cur = list(price_cur)
    href_cur= all_load.values()
    href_cur = list(href_cur)

    with open("all_categories_dict.json", "w") as file:
        json.dump(all_dict, file, indent=4, ensure_ascii=False)

    with open("all_categories_dict.json") as file:
        all_load = json.load(file)
    price_cur_new = all_load.keys()
    price_cur_new = list(price_cur_new)
    href_cur_new= all_load.values()
    href_cur_new = list(href_cur_new)


    print(price_cur[0])
    print(price_cur[0].split(" ")[0])
    print(price_cur_new[0].split(" ")[0])
    print(href_cur[0])
    print(href_cur_new[0])




    if float(price_cur_new[0].split(" ")[0]) <= float(price_cur[0].split(" ")[0]) * 0.8:
        bot.send_message(453039694, text=href_cur_new[0])
        bot.send_message(639191552, text=href_cur_new[0])
        bot.send_message(770387022, text=href_cur_new[0])









    driver.close()
    driver.quit()
    sleep(30)



