from django.conf import settings
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

line_bot_api = LineBotApi('ZnFx4dn7xECPlisBxNk16yZS2bOphDdMNKCXm2VOMaHHtjKbEkfWTt6fxDVAZVuXl5Wr3CIHE4J3FYeqv/I/fPJ3UBCjYAAhlZK2hSgw3LN8JeN2BqHVZsW9CEPHRtQRCM7ZzI/zm3/owADNERLy4QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('d4b77968c644b0f22c57fba9abdd5488')


@csrf_exempt
def callback(request):

    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                line_bot_api.reply_message(
                    event.reply_token,
                   TextSendMessage(text=event.message.text)
                )
        return HttpResponse()
    else:
        return HttpResponseBadRequest()