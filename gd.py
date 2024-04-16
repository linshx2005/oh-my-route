import requests
from datetime import datetime  
lis = './lis.json'
dk = 'dk.json'
# 获取今天的日期  
today = datetime.today()  
  
# 获取今天是今年的第几天  
day = today.timetuple().tm_yday  

try:  
    with open(lis, 'r') as f:  
        li = eval(f.read())  
except FileNotFoundError:  
    print('1')
day2 = day - 9

try:  
    with open(dk, 'r') as f:  
        du = eval(f.read())  
except FileNotFoundError:  
    print('2')
day1 = day - 6
  
def send_server_chan_notification(access_token, title, content):  
    """  
    向Server酱发送POST通知  
  
    :param access_token: Server酱的access_token  
    :param title: 通知的标题  
    :param content: 通知的内容  
    """  
    url = "https://sctapi.ftqq.com/" + access_token + ".send"  
    data = {  
        "text": content,  
        "desp": content,  # 有些Server酱版本可能需要这个字段  
    }  
    if title:  
        data["title"] = title  
  
    headers = {  
        "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"  
    }  
  
    response = requests.post(url, data=data, headers=headers)
    
def push_message(title, content):
    # PushPlus API Token
    api_token = 'c204e4622c9f4e3e8bf06591c7f6e89d'
 
    # PushPlus请求URL
    url = 'http://www.pushplus.plus/send'
 
    # 发送POST请求
    data = {
        "token": api_token,
        "title": title,
        "content": content
    }
 
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("消息推送成功")
        else:
            print("消息推送失败")
    except requests.exceptions.RequestException as e:
        print("消息推送出错:", e)    
# 使用示例  
if __name__ == "__main__":  
    ACCESS_TOKEN = "SCT242760TeNxiWHrdLtFYqmJkeQnqE2Xq"  
    TITLE = "vc"
    TITLE1 = "dk"  
    CONTENT = "vc\n6776513150\n6753671485"
    CONTENT1 = 'dk\n6776513150\n6753671485'
    li.append(day)
    del li[0]
    with open(lis, 'w') as f:  
        f.write(str(li))        
