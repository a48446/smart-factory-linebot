import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
from datetime import datetime

options = Options()
prefs = {
    'profile.default_content_setting_values' :
        {
        'notifications' : 2
        }
}
options.add_experimental_option('prefs',prefs)#禁用瀏覽器彈窗
options.add_argument("--incognito")           #開啟無痕模式
options.add_argument("--headless")      #不開啟實體瀏覽器背景執行
driver = webdriver.Chrome(options=options)
driver.get("https://www.cwb.gov.tw/V8/C/W/Town/Town.html?TID=6600500") #南投名間鄉
Temp = driver.find_element_by_id('tem-C no-unit is-active').text 
abc = driver.find_element_by_id('signal').text
print (abc)