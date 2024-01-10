import requests#13

url1="http://sage-accessible-hub.glitch.me";

url2="http://meowing-melodious-crab.glitch.me";

url3="https://glitchyyb.deno.dev";

url4="https://ggyyb.deno.dev";


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

