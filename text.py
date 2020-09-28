import requests
from pymongo import MongoClient
from bs4 import BeautifulSoup
from bson.objectid import ObjectId

client = MongoClient("mongodb://nutc.iot:nutciot5891@ds237922.mlab.com:37922/smart-data-center",retryWrites="false")
db = client["smart-data-center"]

#mongoDB資料庫
dl303data = db.dl303
upsAdata = db.ups_A
upsBdata = db.ups_B
RoomPowerdata = db.computerRoomPower
RoomInformationdata = db.computerRoomInformation
serviceListdata = db.serviceList
controldata = db.control
data_objectid = '5e61ca5964e2e44b2dabd5ea'

roomdata = RoomInformationdata.find_one({'_id': ObjectId(data_objectid)},{ "_id": 0})
print(roomdata)


myquery = { "_id": ObjectId(data_objectid)}
newvalues = { "$set": { 
                  "disk":30,
                  "pc":40,
                  "ram":50,
                  "sdnSwitch":60
                      }
                  }
RoomInformationdata.update_one(myquery, newvalues)