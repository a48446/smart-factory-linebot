import os
import requests
import json
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime

line_bot_api = LineBotApi('q7TWa/81a0nmW9GnqF6+u8qaFoMbi6q3Dq5VK2QM7FV8UIx3nQk5+luk5GpASk/bm5qtAmimAyA2/Ifdg6a0hH3dwMdfdAoRiGE8TF/IiRXriLsK7j9FDHlQUC34zr7EXiktLqyT5btGhtCTJXbTZQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler("57141ec8f7ba725d4fa3fa97a5bd5169")

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            messages = (
                "Invalid signature. Please check your channel access token/channel secret."
            )
            logger.error(messages)
            return HttpResponseBadRequest(messages)
        return HttpResponse("OK")

@handler.add(event=MessageEvent, message=TextMessage)
def handl_message(event):
    outInfo = "汪汪"
    # outInfo = crawler("content")
    message = TextSendMessage(text=outInfo)
    line_bot_api.reply_message(
        event.reply_token,
        message)

def crawler(content):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get("https://www.cwb.gov.tw/V8/C/W/Town/Town.html?TID=6600500") #南投名間鄉
    Temp = driver.find_element_by_id('tem-C no-unit is-active').text #現在溫度
    bodyTemp = driver.find_element_by_id('GT_C_AT').text #體感溫度
    RelativeHumidity = driver.find_element_by_id('GT_RH').text #相對溼度
    Rain = driver.find_element_by_id('GT_Rain').text #降雨量
    Sunrise = driver.find_element_by_id('GT_Sunrise').text #日出時間
    Sunset = driver.find_element_by_id('GT_Sunset').text
    driver.quit()
    time = datetime.now()
    timeprint = datetime.strftime(time,"%Y/%m/%d %H:%M")
    content = ""
    content="【名間鄉當前天氣概況】"+"\n"+"\n"+"現在溫度 : "+Temp+"°C"+"\n"+"體感溫度 : "+bodyTemp+"°C"+"\n"+"相對溼度 : "+RelativeHumidity+"%"+"\n"+"降雨量 : "+Rain+"mm"+"\n"+"日出時間 : "+Sunrise+"\n"+"日落時間 : "+Sunset + "\n"+"現在時間為："+timeprint
    # content = ""
    # content = "現在溫度:%s 體感溫度:%s 相對溼度:%s 降雨量:%s 日出時間:%s 日落時間:%s"%(Temp, bodyTemp, RelativeHumidity, Rain, Sunrise, Sunset)
    # content= {
    #     "現在溫度":Temp,
    #     "體感溫度":bodyTemp,
    #     "相對溼度":RelativeHumidity,
    #     "降雨量":Rain,
    #     "日出時間":Sunrise,
    #     "日落時間":Sunset
    # }
    # print(content)
    return content
    