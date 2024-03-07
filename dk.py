import requests
from datetime import datetime

dt = datetime.now()
dt = dt.strftime('%j')
dt = int(dt)
print(dt)
l = [67]
l.append(dt)
print(l)
with open('1.txt','wb') as x
    x.write(l)
with open('1.txt','wb') as y
    con = y.read()
    print(con)
x = 6
def send_server_chan_notification(access_token, title, content):
    url = "https://sctapi.ftqq.com/" + access_token + ".send"  
    data = {  
        "text": content,  
        "desp": content,  
    }  
    if title:  
        data["title"] = title  
  
    headers = {  
        "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"  
    }  
  
    response = requests.post(url, data=data, headers=headers)
    
def push_message(title, content):
    
    api_token = 'c204e4622c9f4e3e8bf06591c7f6e89d'
 
    
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
    if x == 7:
        ACCESS_TOKEN = "SCT227782TMxJlx5YE887DkDfBcQ93prou"  
        TITLE = "dkgibaoxidk243566"  
        CONTENT = "vc6776513150vc6753671485"
        push_message(TITLE, CONTENT)
        send_server_chan_notification(ACCESS_TOKEN, TITLE, CONTENT)
    else:
        print(1)    
  
