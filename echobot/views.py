from django.conf import settings
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest , HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from django.views.decorators.http import require_POST


line_bot_api = LineBotApi('q7TWa/81a0nmW9GnqF6+u8qaFoMbi6q3Dq5VK2QM7FV8UIx3nQk5+luk5GpASk/bm5qtAmimAyA2/Ifdg6a0hH3dwMdfdAoRiGE8TF/IiRXriLsK7j9FDHlQUC34zr7EXiktLqyT5btGhtCTJXbTZQdB04t89/1O/w1cDnyilFU=')
parser = WebhookHandler("57141ec8f7ba725d4fa3fa97a5bd5169")

@csrf_exempt
@require_POST
def callback(request: HttpRequest):
    signature = request.headers["X-Line-Signature"]
    body = request.body.decode()

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        messages = (
            "Invalid signature. Please check your channel access token/channel secret."
        )
        logger.error(messages)
        return HttpResponseBadRequest(messages)
    return HttpResponse("OK")

def handl_message(event: MessageEvent):
      line_bot_api.reply_message(
          reply_token=event.reply_token,
          messages=TextSendMessage(text=event.message.text),
      )
def crawler():
    if 1:
        options = Options()
        #關閉瀏覽器跳出訊息
        prefs = {
            'profile.default_content_setting_values' :
                {
                'notifications' : 2
                }
        }
        options.add_experimental_option('prefs',prefs)
        options.add_argument("--headless")            #不開啟實體瀏覽器背景執行
        options.add_argument("--incognito")           #開啟無痕模式
        driver = webdriver.Chrome(options=options)
        driver.get("https://www.cwb.gov.tw/V8/C/W/Town/Town.html?TID=1000806") #南投名間鄉
        Temp = driver.find_element_by_id('GT_C_T').text #現在溫度
        bodyTemp = driver.find_element_by_id('GT_C_AT').text #體感溫度
        RelativeHumidity = driver.find_element_by_id('GT_RH').text #相對溼度
        Rain = driver.find_element_by_id('GT_Rain').text #降雨量
        Sunrise = driver.find_element_by_id('GT_Sunrise').text #日出時間
        Sunset = driver.find_element_by_id('GT_Sunset').text
        driver.quit()
        content= {
            "現在溫度":Temp,
            "體感溫度":bodyTemp,
            "相對溼度":RelativeHumidity,
            "降雨量":Rain,
            "日出時間":Sunrise,
            "日落時間":Sunset
                }
        # print(content)
        return content
    else:
        message = {"no"}
        return message


# @handler.add(MessageEvent, message=TextMessage)
# def message_text(event):
#     a = crawler()
#     line_bot_api.reply_message(
#         event.reply_token,
#         TextSendMessage(text="hello")
#     )