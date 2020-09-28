import os
import json
from bson.objectid import ObjectId
from datetime import datetime
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage ,TemplateSendMessage,ButtonsTemplate,MessageTemplateAction,PostbackEvent
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .message import Featuresmodel , returnvalue  , controlwind , roomlable , roomResourceslable , Dailynews  , roomset , RoomInformationdata


line_bot_api = LineBotApi('q7TWa/81a0nmW9GnqF6+u8qaFoMbi6q3Dq5VK2QM7FV8UIx3nQk5+luk5GpASk/bm5qtAmimAyA2/Ifdg6a0hH3dwMdfdAoRiGE8TF/IiRXriLsK7j9FDHlQUC34zr7EXiktLqyT5btGhtCTJXbTZQdB04t89/1O/w1cDnyilFU=')
parser = WebhookParser("57141ec8f7ba725d4fa3fa97a5bd5169")

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
            if isinstance(event, MessageEvent):  # 如果有normal訊息事件

                if event.message.text == "功能列表":
                
                    line_bot_api.reply_message(  # 回復「功能列表」按鈕樣板訊息
                        event.reply_token,
                        Featuresmodel().content()
                    )
                if event.message.text == "控制":
                
                    line_bot_api.reply_message(  # 回復「控制」按鈕輪播訊息
                        event.reply_token,
                        controlwind().returna()
                    )
                if event.message.text == "機房服務列表":
                
                    line_bot_api.reply_message(  # 回復「機房服務列表」按鈕輪播訊息
                        event.reply_token,
                        roomlable().returna()
                    )
                if event.message.text == "設定機房資訊": ##
                    data_objectid = '5e61ca5964e2e44b2dabd5ea'
                    outInfo = "請輸入VCPU數量(顆):"
                    message = TextSendMessage(text=outInfo)
                    line_bot_api.reply_message(
                        event.reply_token,
                        message)
                    
                    if 1:
                        VCPUnewvalue = event.message.text
                        line_bot_api.reply_message(  # 回復「設定機房資訊」VCPU更改訊息
                            event.reply_token,
                            roomset().returna()
                        )
                        if event.message.text == "yes":
                            myquery = { "_id": ObjectId(data_objectid)}
                            newvalues = { "$set": { 
                                            "disk":VCPUnewvalue
                                                }
                                            }
                            RoomInformationdata.update_one(myquery, newvalues)
                            # RAMnewvalue = input("請輸入RAM數量(GB): ")
                        # #     if RAMnewvalue != None:
                        #         line_bot_api.reply_message(  # 回復「設定機房資訊」VCPU更改訊息
                        #             event.reply_token,
                        #             roomset().returnb()
                        #         )
                        #         if event.message.text == "yes":
                        #             myquery = { "_id": ObjectId(data_objectid)}
                        #             newvalues = { "$set": { 
                        #                             "ram":RAMnewvalue
                        #                                 }
                        #                             }
                        #             RoomInformationdata.update_one(myquery, newvalues)
                        #         else:
                        #             RAMnewvalue = input("請輸入RAM數量(GB): ")
                        # else:
                        #     VCPUnewvalue = input("請輸入VCPU數量(顆): ")

                if event.message.text == "查看設定結果":
                    
                    line_bot_api.reply_message(  # 回復「查看設定結果」按鈕輪播訊息
                        event.reply_token,
                        roomResourceslable().returna()
                    )
                if event.message.text == "機房資訊":
                
                    line_bot_api.reply_message(  # 回復「機房資訊」按鈕輪播訊息
                        event.reply_token,
                        roomResourceslable().returna()
                    )
                if event.message.text == "每日通報資訊":
                
                    line_bot_api.reply_message(  # 回復「每日通報資訊」按鈕輪播訊息
                        event.reply_token,
                        Dailynews().returna()
                    )
                if event.message.text == "機房服務列表":
                
                    line_bot_api.reply_message(  # 回復「機房服務列表」按鈕輪播訊息
                        event.reply_token,
                        roomlable().returna()
                    )
                
            elif isinstance(event, PostbackEvent):  # 如果有postback訊息回傳
                # 電流
                if event.postback.data[0] == "電" and event.postback.data[1] == '流':  # 如果回傳值為「電流」

                    line_bot_api.reply_message(  # 回復訊息文字
                        event.reply_token,
                        TextSendMessage(text=returnvalue().conditioning())
                    )

                # 濕度
                elif event.postback.data[0] == "濕" and event.postback.data[1] == '度':

                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=returnvalue().humi())
                    )

                # 溫度
                elif event.postback.data[0] == "溫" and event.postback.data[1] == '度': 
                    
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=returnvalue().temp())
                    )
                # 電錶
                elif event.postback.data[0] == "電" and event.postback.data[1] == '錶': 
                    
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=returnvalue().roomva())
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
    