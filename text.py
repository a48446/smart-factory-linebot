排風風扇
{
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://i.imgur.com/O8lp0mk.png",
    "size": "full",
    "backgroundColor": "#FFEE99"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "排風風扇",
        "weight": "bold",
        "size": "xl"
      },
      {
        "type": "box",
        "layout": "baseline",
        "margin": "md",
        "contents": [
          {
            "type": "text",
            "text": "狀態：",
            "size": "xs",
            "color": "#999999",
            "margin": "xs",
            "flex": 0
          },
          {
            "type": "text",
            "text": "open"
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": []
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "postback",
          "label": "開啟",
          "data": "開啟",
          "displayText": "開啟"
        }
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "postback",
          "label": "關閉",
          "data": "關閉",
          "displayText": "關閉"
        }
      }
    ],
    "flex": 0
  }
}