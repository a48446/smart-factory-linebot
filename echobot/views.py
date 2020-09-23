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

                # 電流
                if event.postback.data[0] == "電" and event.postback.data[1] == '流':  # 如果回傳值為「電流」
                    message = ''
                    for roomdata in RoomPowerdata.find():
                        message ="冷氣目前電流:"+ str(roomdata["airConditioning"])+"(A)"+"\n"+"最後更新時間:" + str(roomdata["time"])+"\n"+"\n"+"ups_A目前電流:" + str(roomdata["upsA"])+"(A)"+"\n"+"ups_B目前電流:"+ str(roomdata["upsB"])+"(A)"+"\n"+"最後更新時間:"+ str(roomdata["time"])
       
                    line_bot_api.reply_message(  # 回復訊息文字
                        event.reply_token,
                        TextSendMessage(text=message)
                    )

                # 濕度
                elif event.postback.data[0] == "濕" and event.postback.data[1] == '度':
                    message=''
                    for humi in dl303data.find():
                        message ="目前機房濕度:"+ str(humi["DL303_humi"])+"(%)"+"\n"+"最後更新時間:" + str(humi["time"])

                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=message)
                    )

                # 溫度
                elif event.postback.data[0] == "溫" and event.postback.data[1] == '度': 
                    message=''
                    for temp in dl303data.find():
                        message ="目前機房溫度:"+ str(temp["DL303_temp"])+"(°C)"+"\n"+"最後更新時間:" + str(temp["time"])
    
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=message)
                    )

                # 控制 (需修改)
                elif event.postback.data[0] == "控" and event.postback.data[1] == '制':
                    message=''
                    for controldata in controldata.find():
                        message = "排風風扇狀態:"+ str(controldata["outputFan"])+"\n"+"進風風扇狀態:" + str(controldata["inputFan"])+"\n""加濕器狀態:" + str(controldata["humidity"])

                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=message)
                    )

                # 設定機房資訊
                elif event.postback.data[0] == "設" and event.postback.data[1] == '定': 
                    message=''
                    for temp in dl303data.find():
                        message ="目前機房溫度:"+ str(temp["DL303_temp"])+"(°C)"+"\n"+"最後更新時間:" + str(temp["time"])+"\n"
    
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=message)
                    )    

                # 查看機房資訊
                elif event.postback.data[0] == "查" and event.postback.data[5] == '訊': 
                    message=''
                    for temp in dl303data.find():
                        message ="目前機房溫度:"+ str(temp["DL303_temp"])+"(°C)"+"\n"+"最後更新時間:" + str(temp["time"])+"\n"
    
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=message,
                        color= "#0066cc"
                        )
                    )

                # 機房資訊
                elif event.postback.data[0] == "機" and event.postback.data[2] == '資': 
                    message = ""
                    for computerdata in RoomInformationdata.find():
                        message ="VCPU數量(顆):"+ str(computerdata["vcpu"])+"\n"+"RAM數量(GB):"+ str(computerdata["ram"])+"\n"+"機房儲存空間(TB):"+ str(computerdata["disk"])+"\n"+"機房Switch數量(台):"+ str(computerdata["switch"])+"\n"+"機房SDN Switch 數量(台):"+ str(computerdata["sdnSwitch"])+"\n"+"機房一般主機數量(台):"+ str(computerdata["pc"])+"\n"+"機房伺服器數量(台):"+ str(computerdata["server"])
      
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=message)
                    )

                # 每日通報資訊
                elif event.postback.data[0] == "每" and event.postback.data[1] == '日': 
                    message = ''
                    url = "https://www.cwb.gov.tw/V8/C/W/Town/MOD/Week/6600500_Week_PC.html?T=2020091716-4"
                    html = requests.get(url)
                    s = BeautifulSoup(html.text, 'html.parser')
                    for Noticedata in RoomPowerdata.find():
                        timerange = str(Noticedata["cameraStartTime"])[0:4] + "~" + str(Noticedata["cameraEndTime"])[0:4]
                        weatherword = s.find(class_="signal").find('img').get('title')
                        rain = s.find(headers="day1 rainful d1d").text
                        maxa = s.find(class_="tem-C is-active").text[0:3]
                        maxb = s.find(class_="tem-C is-active").text[5:7]
                        maxtemp = ""
                        mina = s.find(headers="day1 lo-temp d1n").text[0:3]
                        minb = s.find(headers="day1 lo-temp d1n").text[5:7]
                        mintemp = ''
                        if maxa > maxb :
                            maxtemp = maxa
                        else:
                            maxtemp = maxb
                        if mina > minb :
                            mintemp = minb
                        else:
                            mintemp = mina

                        message ="昨日冷氣消耗"+ str(Noticedata["airConditioning"])+"度"+"\n"+"昨日ups_A消耗:" + str(Noticedata["upsA"])+"度"+"\n"+"昨日ups_B消耗:" + str(Noticedata["upsB"])+"度"+"\n"+"昨日水塔馬達消耗:"+ str(Noticedata["waterTank"])+"度"+"\n"+"前天電錶數值:"+ str(Noticedata["cameraPowerBeforeDay2"])+"度"+"\n"+"昨日電錶數值:"+ str(Noticedata["cameraPowerBeforeDay1"])+"度"+"\n"+"昨日電錶數值:"+ str(Noticedata["cameraPower"])+"度"+"\n"+"昨日電錶消耗:"+ str(Noticedata["cameraPowerConsumption"])+"度"+"\n" + timerange + "\n" + "天氣:" + weatherword + "\n" +"最低溫度:" + mintemp+ "°C" + "\n" + "最高溫度:" + maxtemp+ "°C" +"\n" + "降雨機率:" + rain

                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=message)
                    )

                # 機房服務列表
                elif event.postback.data[2] == "服" and event.postback.data[3] == '務': 
                    urldata = []
                    namedata = []
                    accpasdata= []
                    statusdata = []
                    serviceList = ""
                    for serviceList in serviceListdata.find():
                        name = serviceList["name"]
                        url = serviceList["url"]
                        accpas = serviceList["notice"]
                        status = serviceList["enabled"]
                        namedata.append(name)
                        urldata.append(url)
                        accpasdata.append(accpas)
                        statusdata.append(status)

                    #ICINGA
                    ICINGA ="服務名稱"+ str(namedata[0])+"\n"+"服務網址"+ str(urldata[0])+"\n"+"服務啟用狀態:" + str(statusdata[0])+"\n"+"備註:"+ str(accpasdata[0])
                    #Kubernetes Dashboard
                    Kubernetes="服務名稱"+ str(namedata[1])+"\n"+"服務網址"+ str(urldata[1])+"\n"+"服務啟用狀態:" + str(statusdata[1])
                    #Ceph
                    Ceph="服務名稱"+ str(namedata[2])+"\n"+"服務網址"+ str(urldata[2])+"\n"+"服務啟用狀態:" + str(statusdata[2])
                    #機房環控分析系統
                    room="服務名稱"+ str(namedata[3])+"\n"+"服務網址"+ str(urldata[3])+"\n"+"服務啟用狀態:" + str(statusdata[3])
                    #Elastsearch Dashboard
                    Elastsearch="服務名稱"+ str(namedata[4])+"\n"+"服務網址"+ str(urldata[4])+"\n"+"服務啟用狀態:" + str(statusdata[4])
                    #CORD
                    CORD="服務名稱"+ str(namedata[5])+"\n"+"服務網址"+ str(urldata[5])+"\n"+"服務啟用狀態:" + str(statusdata[5])
                    #smart-data-center
                    smart="服務名稱"+ str(namedata[6])+"\n"+"服務網址"+ str(urldata[6])+"\n"+"服務啟用狀態:" + str(statusdata[6])
                    #S3 Portal
                    s3="服務名稱"+ str(namedata[7])+"\n"+"服務網址"+ str(urldata[7])+"\n"+"服務啟用狀態:" + str(statusdata[7])
                    #Grafana-ups_route_current
                    Grafana="服務名稱"+ str(namedata[8])+"\n"+"服務網址"+ str(urldata[8])+"\n"+"服務啟用狀態:" + str(statusdata[8])
                    #Lora vehicle platform
                    Lora="服務名稱"+ str(namedata[9])+"\n"+"服務網址"+ str(urldata[9])+"\n"+"服務啟用狀態:" + str(statusdata[9])
                    #Private Ethereum
                    Private="服務名稱"+ str(namedata[10])+"\n"+"服務網址"+ str(urldata[10])+"\n"+"服務啟用狀態:" + str(statusdata[10])
                    #Tensorboard
                    Tensorboard="服務名稱"+ str(namedata[11])+"\n"+"服務網址"+ str(urldata[11])+"\n"+"服務啟用狀態:" + str(statusdata[11])

                    message = ICINGA+ "\n" + "\n"+ Kubernetes + "\n" +"\n"+ Ceph + "\n" +"\n"+ room + "\n" +"\n"+Elastsearch+ "\n" +"\n"+CORD+"\n"+ "\n"+smart+"\n"+ "\n"+s3+"\n"+ "\n"+Grafana+"\n"+ "\n"+Lora+"\n"+ "\n"+Private+"\n"+ "\n"+Tensorboard+"\n"+ "\n"

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
    