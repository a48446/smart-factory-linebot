from abc import ABC, abstractmethod
from linebot.models import TemplateSendMessage , ButtonsTemplate, PostbackTemplateAction

# 訊息抽象類別
class Message(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def content(self):
        pass

# 「選擇地區」按鈕樣板訊息
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
                    )
                ]
            )
        )
        return body


