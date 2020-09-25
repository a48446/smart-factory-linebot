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

controlprintdata = []
for data in controldata.find():
    controlprintdata = data
print(controlprintdata)   