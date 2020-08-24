# -*- coding: UTF-8 -*-
import requests
import twder
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
USD=twder.now('USD')             #顯示美金匯率
EUR=twder.now('EUR')             #顯示歐元匯率
CNY=twder.now('CNY')             #顯示人民幣匯率
#JPY=twder.now('JPY')            #顯示日元匯率
#KRW=twder.now('KRW')            #顯示韓元匯率
def send_ifttt(v1,v2,v3):   
    url = ('https://maker.ifttt.com/trigger/ya0933632805/with/key/n3N74U8Tpqk3L9DzllsTIReD6dIvym2agyMYZjGbyRX' +
          '?value1='+str(v1)+
          '&value2='+str(v2)+
          '&value3='+str(v3))
    r = requests.get(url)      
    if r.text[:5] == 'Congr':  
        print('已傳送 ('+str(v1)+','+str(v2)+','+str(v3)+') 到 Line')
    return r.text
ret = send_ifttt(USD,EUR,CNY)  
print('IFTTT 的回應訊息：',ret)     