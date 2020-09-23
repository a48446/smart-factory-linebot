import os
import json
import requests
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
from bs4 import BeautifulSoup
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage ,TemplateSendMessage,ButtonsTemplate,MessageTemplateAction,PostbackEvent
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .message import Featuresmodel

line_bot_api = LineBotApi('q7TWa/81a0nmW9GnqF6+u8qaFoMbi6q3Dq5VK2QM7FV8UIx3nQk5+luk5GpASk/bm5qtAmimAyA2/Ifdg6a0hH3dwMdfdAoRiGE8TF/IiRXriLsK7j9FDHlQUC34zr7EXiktLqyT5btGhtCTJXbTZQdB04t89/1O/w1cDnyilFU=')
parser = WebhookParser("57141ec8f7ba725d4fa3fa97a5bd5169")

client = MongoClient("mongodb://nutc.iot:nutciot5891@ds237922.mlab.com:37922/smart-data-center")
db = client["smart-data-center"]

#mongoDB資料庫
dl303data = db.dl303
upsAdata = db.ups_A
upsBdata = db.ups_B
RoomPowerdata = db.computerRoomPower
RoomInformationdata = db.computerRoomInformation
serviceListdata = db.serviceList
controldata = db.control

@csrf_exempt
def callback(request):

    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):  # 如果有訊息事件

                if event.message.text == "功能列表":

                    line_bot_api.reply_message(  # 回復「功能列表」按鈕樣板訊息
                        event.reply_token,
                        Featuresmodel().content()
                    )

            elif isinstance(event, PostbackEvent):  # 如果有訊息回傳

                if event.postback.data[0] == "電" and event.postback.data[1] == '流':  # 如果回傳值為「電流」
                    message = ''
                    for roomdata in RoomPowerdata.find():
                        message ="冷氣目前電流:"+ str(roomdata["airConditioning"])+"(A)"+"\n"+"最後更新時間:" + str(roomdata["time"])+"\n"+"\n"+"ups_A目前電流:" + str(roomdata["upsA"])+"(A)"+"\n"+"ups_B目前電流:"+ str(roomdata["upsB"])+"(A)"+"\n"+"最後更新時間:"+ str(roomdata["time"])+"\n"
       
                    line_bot_api.reply_message(  # 回復訊息文字
                        event.reply_token,
                        TextSendMessage(text=message)
                    )

                elif event.postback.data[0] == "濕" and event.postback.data[1] == '度':
                    message=''
                    for humi in dl303data.find():
                        message ="目前機房濕度:"+ str(humi["DL303_humi"])+"(%)"+"\n"+"最後更新時間:" + str(humi["time"])+"\n"

                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=message)
                    )
                elif event.postback.data[0] == "溫" and event.postback.data[1] == '度': 
                    message=''
                    for temp in dl303data.find():
                        message ="目前機房溫度:"+ str(temp["DL303_temp"])+"(°C)"+"\n"+"最後更新時間:" + str(temp["time"])+"\n"
    
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=message)
                    )

        return HttpResponse()
    else:
        return HttpResponseBadRequest()

# @csrf_exempt
# def callback(request):
#     if request.method == 'POST':
#         signature = request.META['HTTP_X_LINE_SIGNATURE']
#         body = request.body.decode('utf-8')
#         try:
#             handler.handle(body, signature)
#         except InvalidSignatureError:
#             messages = (
#                 "Invalid signature. Please check your channel access token/channel secret."
#             )
#             logger.error(messages)
#             return HttpResponseBadRequest(messages)
#         return HttpResponse("OK")

# @handler.add(event=MessageEvent, message=TextMessage)
# def handl_message(event):
#     # outInfo = "汪汪"
#     outInfo = crawler("content")
#     message = TextSendMessage(text=outInfo)
#     line_bot_api.reply_message(
#         event.reply_token,
#         message)

# def crawler(content):
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--disable-dev-shm-usage")
#     chrome_options.add_argument("--no-sandbox")
#     driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
#     driver.get("https://www.cwb.gov.tw/V8/C/W/Town/Town.html?TID=6600500") #南投名間鄉
#     Temp = driver.find_element_by_id('GT_C_T').text #現在溫度
#     bodyTemp = driver.find_element_by_id('GT_C_AT').text #體感溫度
#     RelativeHumidity = driver.find_element_by_id('GT_RH').text #相對溼度
#     Rain = driver.find_element_by_id('GT_Rain').text #降雨量
#     Sunrise = driver.find_element_by_id('GT_Sunrise').text #日出時間
#     Sunset = driver.find_element_by_id('GT_Sunset').text
#     driver.quit()
#     time = datetime.now()
#     timeprint = datetime.strftime(time,"%Y/%m/%d %H:%M")
#     content = ""
#     content="【名間鄉當前天氣概況】"+"\n"+"\n"+"現在溫度 : "+Temp+"°C"+"\n"+"體感溫度 : "+bodyTemp+"°C"+"\n"+"相對溼度 : "+RelativeHumidity+"%"+"\n"+"降雨量 : "+Rain+"mm"+"\n"+"日出時間 : "+Sunrise+"\n"+"日落時間 : "+Sunset + "\n"+"現在時間為："+timeprint
#     # content = ""
#     # content = "現在溫度:%s 體感溫度:%s 相對溼度:%s 降雨量:%s 日出時間:%s 日落時間:%s"%(Temp, bodyTemp, RelativeHumidity, Rain, Sunrise, Sunset)
#     # content= {
#     #     "現在溫度":Temp,
#     #     "體感溫度":bodyTemp,
#     #     "相對溼度":RelativeHumidity,
#     #     "降雨量":Rain,
#     #     "日出時間":Sunrise,
#     #     "日落時間":Sunset
#     # }
#     # print(content)
#     return content
    