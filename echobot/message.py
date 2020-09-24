import requests
from abc import ABC, abstractmethod
from linebot.models import TemplateSendMessage , ButtonsTemplate, PostbackAction , MessageAction , URIAction , CarouselColumn , CarouselTemplate , PostbackTemplateAction , FlexSendMessage
from pymongo import MongoClient
from bs4 import BeautifulSoup

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

# 訊息抽象類別
class Message(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def content(self):
        pass

# # 「功能列表」按鈕樣板訊息
# class Featuresmodel(Message):
#     def content(self):
#         body = TemplateSendMessage(
#             alt_text='Buttons template',
#             template=ButtonsTemplate(
#                 title='功能列表',
#                 text='請選擇想要使用的功能',
#                 actions=[
#                     PostbackTemplateAction(
#                         label='電流',
#                         text='電流',
#                         data='電流'
#                     ),
#                     PostbackTemplateAction(
#                         label='濕度',
#                         text='濕度',
#                         data='濕度'
#                     ),
#                     PostbackTemplateAction(
#                         label='溫度',
#                         text='溫度',
#                         data='溫度'
#                     ),
#                     PostbackTemplateAction(
#                         label='控制',
#                         text='控制',
#                         data='控制'
#                     )
#                 ]
#             )
#         )
#         body2 = TemplateSendMessage(
#             alt_text='Buttons template',
#             template=ButtonsTemplate(
#                 title='功能列表',
#                 text='請選擇想要使用的功能',
#                 actions=[
#                     PostbackTemplateAction(
#                         label='設定機房資訊',
#                         text='設定機房資訊',
#                         data='設定機房資訊'
#                     ),
#                     PostbackTemplateAction(
#                         label='查看機房資訊',
#                         text='查看機房資訊',
#                         data='查看機房資訊'
#                     ),
#                     PostbackTemplateAction(
#                         label='機房資訊',
#                         text='機房資訊',
#                         data='機房資訊'
#                     ),
#                     PostbackTemplateAction(
#                         label='每日通報資訊',
#                         text='每日通報資訊',
#                         data='每日通報資訊'
#                     )
#                 ]
#             )
#         )
#         body3 = TemplateSendMessage(
#             alt_text='Buttons template',
#             template=ButtonsTemplate(
#                 title='功能列表',
#                 text='請選擇想要使用的功能',
#                 actions=[
#                     PostbackTemplateAction(
#                         label='機房服務列表',
#                         text='機房服務列表',
#                         data='機房服務列表'
#                     )
#                 ]
#             )
#         )
#         return body , body2 , body3

# 「功能列表」按鈕樣板訊息
class Featuresmodel(Message):
    def content(self):
        body = FlexSendMessage(
            alt_text='hello',
            contents={
                "type": "bubble",
                "size": "mega",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "功能列表",
                            "color": "#ffffff",
                            "size": "xl",
                            "flex": 4,
                            "weight": "regular",
                            "margin": "xs"
                        }
                        ]
                    }
                    ],
                    "paddingAll": "20px",
                    "backgroundColor": "#0367D3",
                    "spacing": "md",
                    "height": "80px",
                    "paddingTop": "22px"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "postback",
                            "label": "電流",
                            "data": "電流",
                            "displayText": "電流"
                            },
                            "color": "#ffffff"
                        }
                        ],
                        "backgroundColor": "#0367D3"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "postback",
                            "label": "濕度",
                            "data": "濕度",
                            "displayText": "濕度"
                            },
                            "color": "#ffffff"
                        }
                        ],
                        "backgroundColor": "#0367D3"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "postback",
                            "label": "溫度",
                            "data": "溫度",
                            "displayText": "溫度"
                            },
                            "color": "#ffffff"
                        }
                        ],
                        "backgroundColor": "#0367D3"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "控制",
                            "text": "控制"
                            },
                            "color": "#ffffff"
                        }
                        ],
                        "backgroundColor": "#0367D3"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "postback",
                            "label": "設定機房資訊",
                            "data": "設定機房資訊",
                            "displayText": "設定機房資訊"
                            },
                            "color": "#ffffff"
                        }
                        ],
                        "backgroundColor": "#0367D3"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "postback",
                            "label": "查看機房資訊",
                            "data": "查看機房資訊",
                            "displayText": "查看機房資訊"
                            },
                            "color": "#ffffff"
                        }
                        ],
                        "backgroundColor": "#0367D3"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "postback",
                            "label": "機房資訊",
                            "data": "機房資訊",
                            "displayText": "機房資訊"
                            },
                            "color": "#ffffff"
                        }
                        ],
                        "backgroundColor": "#0367D3"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "postback",
                            "label": "每日通報資訊",
                            "data": "每日通報資訊",
                            "displayText": "每日通報資訊"
                            },
                            "color": "#ffffff"
                        }
                        ],
                        "backgroundColor": "#0367D3"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "postback",
                            "label": "機房服務列表",
                            "data": "機房服務列表",
                            "displayText": "機房服務列表"
                            },
                            "color": "#ffffff"
                        }
                        ],
                        "backgroundColor": "#0367D3"
                    }
                    ],
                    "spacing": "xs"
                }
                }
            )
        return body

# 按鈕回傳值
class returnvalue():
    #電流
    def conditioning(self):
        message = ''
        for roomdata in RoomPowerdata.find():
            message ="冷氣目前電流:"+ str(roomdata["airConditioning"])+"(A)"+"\n"+"最後更新時間:" + str(roomdata["time"])+"\n"+"\n"+"ups_A目前電流:" + str(roomdata["upsA"])+"(A)"+"\n"+"ups_B目前電流:"+ str(roomdata["upsB"])+"(A)"+"\n"+"最後更新時間:"+ str(roomdata["time"])

        return message
    #濕度
    def humi(self):
        message=''
        for humi in dl303data.find():
            message ="目前機房濕度:"+ str(humi["DL303_humi"])+"(%)"+"\n"+"最後更新時間:" + str(humi["time"])

        return message
    #溫度
    def temp(self):
        message=''
        for temp in dl303data.find():
            message ="目前機房溫度:"+ str(temp["DL303_temp"])+"(°C)"+"\n"+"最後更新時間:" + str(temp["time"])

        return message
    #控制
    def control(self):
        message=''
        for controldata in controldata.find():
            message = "排風風扇狀態:"+ str(controldata["outputFan"])+"\n"+"進風風扇狀態:" + str(controldata["inputFan"])+"\n""加濕器狀態:" + str(controldata["humidity"])

        return message
    #設定機房資訊
    def setroomdata(self):
        message=''
        for temp in dl303data.find():
            message ="目前機房溫度:"+ str(temp["DL303_temp"])+"(°C)"+"\n"+"最後更新時間:" + str(temp["time"])+"\n"

        return message
    #查看機房資訊
    def watchroomdata(self):
        message=''
        for temp in dl303data.find():
            message ="目前機房溫度:"+ str(temp["DL303_temp"])+"(°C)"+"\n"+"最後更新時間:" + str(temp["time"])+"\n"

        return message
    #機房資訊
    def roomdata(self):
        message = ""
        for computerdata in RoomInformationdata.find():
            message ="VCPU數量(顆):"+ str(computerdata["vcpu"])+"\n"+"RAM數量(GB):"+ str(computerdata["ram"])+"\n"+"機房儲存空間(TB):"+ str(computerdata["disk"])+"\n"+"機房Switch數量(台):"+ str(computerdata["switch"])+"\n"+"機房SDN Switch 數量(台):"+ str(computerdata["sdnSwitch"])+"\n"+"機房一般主機數量(台):"+ str(computerdata["pc"])+"\n"+"機房伺服器數量(台):"+ str(computerdata["server"])

        return message
    #每日通報
    def Dailynews(self):
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

        return message
    #機房服務列表
    def servicelist(self):
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
        return message


class textmodel():
    def returna(self):
        flex_message = FlexSendMessage(
            alt_text='hello',
            contents={
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://i.imgur.com/O8lp0mk.png",
                "size": "full",
                "backgroundColor": "#FFEE99"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "排風風扇",
                    "weight": "bold",
                    "size": "xl"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "margin": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": "狀態：",
                        "size": "xs",
                        "color": "#999999",
                        "margin": "xs",
                        "flex": 0
                    },
                    {
                        "type": "text",
                        "text": "open"
                    }
                    ]
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "lg",
                    "spacing": "sm",
                    "contents": []
                }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                    "type": "postback",
                    "label": "開啟",
                    "data": "開啟",
                    "displayText": "開啟"
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                    "type": "postback",
                    "label": "關閉",
                    "data": "關閉",
                    "displayText": "關閉"
                    }
                }
                ],
                "flex": 0
                }
            }
        )
        return flex_message

