from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import requests
from bs4 import BeautifulSoup as bs
import json
import time
import schedule
def get_menu(s):
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    }
    html = session.get('https://www.kaist.ac.kr/kr/html/campus/053001.html?dvs_cd=icc', headers=headers).content
    soup = bs(html, "html.parser")
    dic = {'breakfast': '#tab_item_1 > table > tbody > tr > td:nth-child(1)',
    'lunch': '#tab_item_1 > table > tbody > tr > td:nth-child(2)',
    'dinner': '#tab_item_1 > table > tbody > tr > td:nth-child(3)',
    'title': '#tab_item_1 > h3'}
    if s == 'title':
        return soup.select(dic[s])[0].text
    else:
        temp = soup.select(dic[s])[0].text.split()
        return ', '.join(list(map(lambda x: x.replace('*',''), temp)))
def do(token, channel):
    # api 토큰
    token = token
    client = WebClient(token)
    bf = get_menu('breakfast')
    lunch = get_menu('lunch')
    dinner = get_menu('dinner')
    title = get_menu('title')
    text = "*[ 아 침 ]*\n - " + bf +"\n\n*[ 점 심 ]*\n - " + lunch + "\n\n*[ 저 녁 ]*\n - " + dinner
    blocks = [
        {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": '🍗 '+title, 
            "emoji": True
                    }
                },
        {
           "type": "divider"
        },
        {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": text
        },
            "accessory": {
                        "type": "image",
                        "image_url": "https://img.jjang0u.com/data3/chalkadak/160/201902/08/154963177454595.gif",
                "alt_text": ""
        }

    }]
    response = client.chat_postMessage(channel=channel, blocks=blocks)
    

    
token = 'xoxb-1543956691168-3392605655365-cHiW9BN6UyUiCQJ3iQqUZmQo'
channel = '#정글4기_a반_잡담'
schedule.every().day.at("7:00").do(do, token, channel)
while True:
    schedule.run_pending()
    time.sleep(1)