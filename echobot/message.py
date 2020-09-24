from abc import ABC, abstractmethod
from linebot.models import TemplateSendMessage , ButtonsTemplate, PostbackTemplateAction

# 訊息抽象類別
class Message(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def content(self):
        pass

# 「功能列表」按鈕樣板訊息
class Featuresmodel(Message):
    def content(self):
        body = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='功能列表',
                text='請選擇想要使用的功能',
                actions=[
                    PostbackTemplateAction(
                        label='電流',
                        text='電流',
                        data='電流'
                    ),
                    PostbackTemplateAction(
                        label='濕度',
                        text='濕度',
                        data='濕度'
                    ),
                    PostbackTemplateAction(
                        label='溫度',
                        text='溫度',
                        data='溫度'
                    ),
                    PostbackTemplateAction(
                        label='控制',
                        text='控制',
                        data='控制'
                    )
                ]
            )
        )
        body2 = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='功能列表',
                text='請選擇想要使用的功能',
                actions=[
                    PostbackTemplateAction(
                        label='設定機房資訊',
                        text='設定機房資訊',
                        data='設定機房資訊'
                    ),
                    PostbackTemplateAction(
                        label='查看機房資訊',
                        text='查看機房資訊',
                        data='查看機房資訊'
                    ),
                    PostbackTemplateAction(
                        label='機房資訊',
                        text='機房資訊',
                        data='機房資訊'
                    ),
                    PostbackTemplateAction(
                        label='每日通報資訊',
                        text='每日通報資訊',
                        data='每日通報資訊'
                    )
                ]
            )
        )
        body3 = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='功能列表',
                text='請選擇想要使用的功能',
                actions=[
                    PostbackTemplateAction(
                        label='機房服務列表',
                        text='機房服務列表',
                        data='機房服務列表'
                    )
                ]
            )
        )
        return body , body2 , body3

class returnvalue(Message):
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