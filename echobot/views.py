from django.conf import settings
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

line_bot_api = LineBotApi('0Nuv+3Ya4IUjwYt08aegkR7OdblZ2J65U64QHFPey0gKsPRXxMLxPKfk/zJLwsntl5Wr3CIHE4J3FYeqv/I/fPJ3UBCjYAAhlZK2hSgw3LPYm1YC93aIcNRYHSveNKAS4qAaTrI+yVFbYYyE/P3Q/gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('d4b77968c644b0f22c57fba9abdd5488')

@csrf_exempt
@require_POST
def webhook(request: HttpRequest):
    signature = request.headers["X-Line-Signature"]
    body = request.body.decode()

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
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        line_bot_api.reply_message(
            reply_token=event.reply_token,
            messages=TextSendMessage(text=event.message.text),
        )