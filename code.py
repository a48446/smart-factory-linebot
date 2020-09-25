# 推播通知
{
  "type": "bubble",
  "size": "mega",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "每日機房推播通知",
            "color": "#ffffff",
            "size": "xl",
            "flex": 4,
            "weight": "regular",
            "margin": "xs"
          }
        ]
      }
    ],
    "paddingAll": "20px",
    "backgroundColor": "#0367D3",
    "spacing": "md",
    "height": "80px",
    "paddingTop": "22px"
  },
  "hero": {
    "type": "image",
    "url": "https://www.cwb.gov.tw/V8/assets/img/weather_icons/weathers/svg_icon/day/04.svg"
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
            "type": "text",
            "text": "昨日冷氣消耗度數：",
            "color": "#0367D3"
          },
          {
            "type": "text",
            "text": "昨日ups_A消耗度數",
            "color": "#0367D3"
          },
          {
            "type": "text",
            "text": "昨日ups_B消耗度數",
            "color": "#0367D3"
          },
          {
            "type": "text",
            "text": "天氣："
          },
          {
            "type": "text",
            "text": "室外溫度："
          },
          {
            "type": "text",
            "text": "體感溫度："
          },
          {
            "type": "text",
            "text": "濕度："
          }
        ],
        "height": "170px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "特別預報：",
            "color": "#FF0000"
          }
        ]
      }
    ]
  }
}