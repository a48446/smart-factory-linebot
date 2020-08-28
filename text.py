





# @handler.add(MessageEvent, message=TextMessage)
# def message_text(event):
#     a = crawler()
#     line_bot_api.reply_message(
#         event.reply_token,
#         TextSendMessage(text="hello")
#     )
import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def crawler():
    if 1:
        options = Options()
        prefs = {
            'profile.default_content_setting_values' :
                {
                'notifications' : 2
                }
        }
        options.add_experimental_option('prefs',prefs)
        options.add_argument("--incognito")           #開啟無痕模式
        options.add_argument("--headless")      #不開啟實體瀏覽器背景執行
        driver = webdriver.Chrome(options=options)
        driver.get("https://www.cwb.gov.tw/V8/C/W/Town/Town.html?TID=1e000806") #南投名間鄉
        Temp = driver.find_element_by_id('GT_C_T').text #現在溫度
        bodyTemp = driver.find_element_by_id('GT_C_AT').text #體感溫度
        RelativeHumidity = driver.find_element_by_id('GT_RH').text #相對溼度
        Rain = driver.find_element_by_id('GT_Rain').text #降雨量
        Sunrise = driver.find_element_by_id('GT_Sunrise').text #日出時間
        Sunset = driver.find_element_by_id('GT_Sunset').text
        driver.quit()
        content="\n"+"名間鄉天氣概況"+"\n"+"\n"+"現在溫度 : "+Temp+"°C"+"\n"+"體感溫度 : "+bodyTemp+"°C"+"\n"+"相對溼度 : "+RelativeHumidity+"%"+"\n"+"降雨量 : "+Rain+"mm"+"\n"+"日出時間 : "+Sunrise+"\n"+"日落時間 : "+Sunset
        # print(content)
        return content
    else:
        message = {"no"}
        return message

def handl_message():
    a = crawler()
    text = a
    return a


b = handl_message()
print(b)