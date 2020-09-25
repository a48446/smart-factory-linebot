import requests
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
