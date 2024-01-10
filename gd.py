import requests#13

url1="http://sage-accessible-hub.glitch.me";

url2="http://meowing-melodious-crab.glitch.me";

url3="https://glitchyyb.deno.dev";

url4="https://ggyyb.deno.dev";

headers1={

 "Host": "47cds5-3000.csb.app",

    "cache-control": "max-age=0",

    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 

            "User-Agent": "Mozilla/5.0 (Linux; Android 13; V2272A Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/101.0.4951.74 Mobile Safari/537.36", 

    "connection": "keep-alive",
    "x-requested-with": "XBrowser",
    "sec-fetch-site": "none",
    "sec-fetch-mode": "navigate",
    "sec-fetch-dest": "document",
     "sec-fetch-user": "?1",
    
    "referer":"https://47cds5-3000.csb.app/",
"accept-language":"zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",

        "Accept-Encoding": "gzip,deflate",
"Upgrade-Insecure-Requests": "1",

"dnt": "1"}
response1= requests.get(url=url1)
print(response1.text)
response2= requests.get(url=url2)
print(response2.text)
response3= requests.get(url=url3)
print(response3.text) 
response4= requests.get(url=url4)
print(response4.text)






def notice(content):
    token ="c204e4622c9f4e3e8bf06591c7f6e89d"  
    title = "glitch"
    url = f"http://www.pushplus.plus/send?token={token}&title={title}&content={content}&template=html"
    response9=requests.request("GET", url) 
    print(response9.text)
notice(response1.text+response2.text+response3.text+response4.text)  

