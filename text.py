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

message=''
for Noticedata in RoomPowerdata.find():
    message ="電錶今日度數:" + str(Noticedata["cameraPower"])+"(度)" +"\n"+ "最後更新時間:" + str(Noticedata["time"])+"\n"+"\n"+"電錶昨日消耗度數"+str(Noticedata["cameraPowerConsumption"])+"\n"+"計算起始時間："+"\n"+str(Noticedata["cameraStartTime"])+"\n"+"計算終止時間"+"\n"+str(Noticedata["cameraEndTime"])

print(message)   