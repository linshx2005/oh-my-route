# coding=utf-8
import requests
from bs4 import BeautifulSoup
from datetime import datetime

now = datetime.today()
now = now.strftime('%Y-%m-%d')
qbt, tr, trx, jpx, bx =[], [], [], [], []
url, url1, url2, url4, url3 = 'https://qbtr.me/tongren/', 'https://tongrenquan.org/tongren/', 'https://trxs.cc/tongren/', 'https://jpxs123.cc/', 'https://bixiange.top/'

def qbtr(url):
    res = requests.get(url)
    res.encoding = 'gb2312'
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    qbtr3 = soup.find_all('div', class_='bk')
    for re in qbtr3:
        r = re.find('label', class_='date')
        date = r.text
        if date == now:
            p = re.find('h3')
            qbt.append(p.text)
def trq(url1):
    res = requests.get(url1)
    res.encoding = 'gb2312'
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    qbtr3 = soup.find_all('div', class_='bk')
    for re in qbtr3:
        r = re.find('label', class_='date')
        date = r.text
        if date == now:
            p = re.find('h3')
            tr.append(p.text)
def trxs(url2):
    res = requests.get(url2)
    res.encoding = 'gb2312'
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    qbtr3 = soup.find_all('div', class_='bk')
    for re in qbtr3:
        r = re.find('label', class_='date')
        date = r.text
        if date == now:
            p = re.find('h3')
            trx.append(p.text)
def jpxs(url4):
    res = requests.get(url4)
    res.encoding = 'gb2312'
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    qbtr3 = soup.find_all('div', class_='infos')
    for re in qbtr3:
        r = re.find('label', class_='date')
        date = r.text
        if date == now:
            p = re.find('h3')
            jpx.append(p.text)
def bxg(url3):
    res = requests.get(url3)
    res.encoding = 'gb2312'
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    qbtr3 = soup.find_all('div', class_='infos')
    for re in qbtr3:
        r = re.find('label', class_='date')
        date = r.text
        if date == now:
            p = re.find('h3')
            bx.append(p.text)



def server(title, content):
    access_token = "SCT242760TeNxiWHrdLtFYqmJkeQnqE2Xq"
    urls = "https://sctapi.ftqq.com/" + access_token + ".send"
    data = {
        "text": content,
        "desp": content,  # 有些Server酱版本可能需要这个字段
    }
    if title:
        data["title"] = title

    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"
    }


    try:
        response = requests.post(urls, data=data, headers=headers)
        if response.status_code == 200:
            print("server推送成功")
        else:
            print("s消息推送失败")
    except requests.exceptions.RequestException as e:
        print("s消息推送出错:", e)

def pushplus(title, content):
    api_token = 'c204e4622c9f4e3e8bf06591c7f6e89d'

    # PushPlus请求URL
    urlp = 'http://www.pushplus.plus/send'

    # 发送POST请求
    data = {
        "token": api_token,
        "title": title,
        "content": content
    }

    try:
        response = requests.post(urlp, json=data)
        if response.status_code == 200:
            print("pushplus推送成功")
        else:
            print("p消息推送失败")
    except requests.exceptions.RequestException as e:
        print("s消息推送出错:", e)

qbtr(url)
trq(url1)
trxs(url2)
jpxs(url4)
bxg(url3)
TITLE = "同人小说"
CONTENT = f'全本同人{qbt}\n同人圈{tr}\n同人小说{trx}\n精品小说{jpx}\n笔仙阁{bx}'
pushplus(TITLE, CONTENT)
server(TITLE, CONTENT)


