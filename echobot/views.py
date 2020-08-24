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
def callback(request: HttpRequest) -> HttpResponse:
    
    if request.method == "POST":
        # get X-Line-Signature header value
        signature = request.META['HTTP_X_LINE_SIGNATURE']

        # get request body as text
        body = request.body.decode('utf-8')

        # handle webhook body
        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            return HttpResponseBadRequest()

        return HttpResponse()
    else:
        return HttpResponseBadRequest()


@handler.add(MessageEvent, message=TextMessage)
def message_text(event: MessageEvent):
    options = Options()
    #關閉瀏覽器跳出訊息
    prefs = {
        'profile.default_content_setting_values' :
            {
            'notifications' : 2
            }
    }
    options.add_experimental_option('prefs',prefs)
    options.add_argument("--headless")            #不開啟實體瀏覽器背景執行
    options.add_argument("--incognito")           #開啟無痕模式
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.cwb.gov.tw/V8/C/W/Town/Town.html?TID=1000806") #南投名間鄉
    Temp = driver.find_element_by_id('GT_C_T').text
    bodyTemp = driver.find_element_by_id('GT_C_AT').text
    RelativeHumidity = driver.find_element_by_id('GT_RH').text
    Rain = driver.find_element_by_id('GT_Rain').text
    Sunrise = driver.find_element_by_id('GT_Sunrise').text
    Sunset = driver.find_element_by_id('GT_Sunset').text
    driver.quit()

    content="\n"+"名間鄉天氣狀況"+"\n"+"\n"+"現在溫度 : "+Temp+"°C"+"\n"+"體感溫度 : "+bodyTemp+"°C"+"\n"+"相對溼度 : "+RelativeHumidity+"%"+"\n"+"降雨量 : "+Rain+"mm"+"\n"+"日出時間 : "+Sunrise+"\n"+"日落時間 : "+Sunset

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(content)
    )