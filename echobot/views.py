import os
import json
from bson.objectid import ObjectId
from datetime import datetime
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage ,TemplateSendMessage,ButtonsTemplate,MessageTemplateAction,PostbackEvent , FlexSendMessage
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .message import Featuresmodel , returnvalue  , controlwind , roomlable , roomResourceslable , Dailynews , roomset , db , inputreturn


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

                    RoomInformationdata = db.computerRoomInformation
                    data_objectid = '5e61ca5964e2e44b2dabd5ea'
                    line_bot_api.reply_message(
                        event.reply_token,
                        inputreturn().returna()
                        )

                # if  event.message.text[3] == 'V' and event.message.text[6] == 'U':
                    # VCPUnewvalue = event.message.text 
                    # flex_message = FlexSendMessage(
                    # alt_text='hello',
                    # contents={
                    # "type": "bubble",
                    # "header": {
                    #     "type": "box",
                    #     "layout": "vertical",
                    #     "contents": [
                    #     {
                    #         "type": "text",
                    #         "text": "VCPU數量(顆):" + VCPUnewvalue
                    #     }
                    #     ],
                    #     "backgroundColor": "#F0F0F0"
                    # },
                    # "body": {
                    #     "type": "box",
                    #     "layout": "vertical",
                    #     "contents": [
                    #     {
                    #         "type": "box",
                    #         "layout": "vertical",
                    #         "contents": [
                    #         {
                    #             "type": "button",
                    #             "action": {
                    #             "type": "message",
                    #             "label": "yes",
                    #             "text": "yes"
                    #             },
                    #             "position": "absolute",
                    #             "offsetStart": "20px"
                    #         },
                    #         {
                    #             "type": "button",
                    #             "action": {
                    #             "type": "message",
                    #             "label": "no",
                    #             "text": "no"
                    #             },
                    #             "position": "relative",
                    #             "offsetStart": "70px"
                    #         }
                    #         ]
                    #     }
                    #     ]
                    # }
                    # }
                    # )
                    # line_bot_api.reply_message(  # 回復「設定機房資訊」VCPU更改訊息
                    #     event.reply_token,
                    #     flex_message
                    #     )
                    # if event.message.text == "yes":
                    #     myquery = { "_id": ObjectId(data_objectid)}
                    #     newvalues = { "$set": { 
                    #                     "disk":VCPUnewvalue
                    #                         }
                    #                     }
                    #     RoomInformationdata.update_one(myquery, newvalues)
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
                elif event.postback.data[3] == "V" and event.postback.data[6] == 'U': 
                    VCPUnewvalue = event.message.text 
                    flex_message = FlexSendMessage(
                    alt_text='hello',
                    contents={
                    "type": "bubble",
                    "header": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "VCPU數量(顆):" + VCPUnewvalue
                        }
                        ],
                        "backgroundColor": "#F0F0F0"
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
                                "type": "message",
                                "label": "yes",
                                "text": "yes"
                                },
                                "position": "absolute",
                                "offsetStart": "20px"
                            },
                            {
                                "type": "button",
                                "action": {
                                "type": "message",
                                "label": "no",
                                "text": "no"
                                },
                                "position": "relative",
                                "offsetStart": "70px"
                            }
                            ]
                        }
                        ]
                    }
                    }
                    )
                    line_bot_api.reply_message(  # 回復「設定機房資訊」VCPU更改訊息
                        event.reply_token,
                        flex_message
                        )
                    if event.message.text == "yes":
                        myquery = { "_id": ObjectId(data_objectid)}
                        newvalues = { "$set": { 
                                        "disk":VCPUnewvalue
                                            }
                                        }
                        RoomInformationdata.update_one(myquery, newvalues)


        return HttpResponse()
    else:
        return HttpResponseBadRequest()


