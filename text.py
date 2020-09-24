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
#機房資源列表
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
            "text": "機房資源列表",
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
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "VCPU數量(顆):",
        "color": "#0367D3"
      },
      {
        "type": "text",
        "text": "RAM數量(GB):",
        "color": "#0367D3"
      },
      {
        "type": "text",
        "text": "機房儲存空間(TB):",
        "color": "#0367D3"
      },
      {
        "type": "text",
        "text": "機房Switch數量(台):",
        "color": "#0367D3"
      },
      {
        "type": "text",
        "text": "機房SDN Switch 數量(台):",
        "color": "#0367D3"
      },
      {
        "type": "text",
        "text": "機房一般主機數量(台):",
        "color": "#0367D3"
      },
      {
        "type": "text",
        "text": "機房伺服器數量(台):",
        "color": "#0367D3"
      }
    ]
  }
}