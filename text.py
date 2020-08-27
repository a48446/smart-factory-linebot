line_bot_api = LineBotApi('q7TWa/81a0nmW9GnqF6+u8qaFoMbi6q3Dq5VK2QM7FV8UIx3nQk5+luk5GpASk/bm5qtAmimAyA2/Ifdg6a0hH3dwMdfdAoRiGE8TF/IiRXriLsK7j9FDHlQUC34zr7EXiktLqyT5btGhtCTJXbTZQdB04t89/1O/w1cDnyilFU=')
parser = WebhookHandler("57141ec8f7ba725d4fa3fa97a5bd5169")





# @handler.add(MessageEvent, message=TextMessage)
# def message_text(event):
#     a = crawler()
#     line_bot_api.reply_message(
#         event.reply_token,
#         TextSendMessage(text="hello")
#     )

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

line_bot_api = LineBotApi('q7TWa/81a0nmW9GnqF6+u8qaFoMbi6q3Dq5VK2QM7FV8UIx3nQk5+luk5GpASk/bm5qtAmimAyA2/Ifdg6a0hH3dwMdfdAoRiGE8TF/IiRXriLsK7j9FDHlQUC34zr7EXiktLqyT5btGhtCTJXbTZQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler("57141ec8f7ba725d4fa3fa97a5bd5169")

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            messages = (
                "Invalid signature. Please check your channel access token/channel secret."
            )
            logger.error(messages)
            return HttpResponseBadRequest(messages)
        return HttpResponse("OK")

@handler.add(event=MessageEvent, message=TextMessage)
def handl_message(event: MessageEvent):
    line_bot_api.reply_message(
        reply_token=event.reply_token,
        messages=TextSendMessage(text=event.message.text),
    )