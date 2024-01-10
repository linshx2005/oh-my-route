import requests#13

url1="http://sage-accessible-hub.glitch.me";

url2="http://meowing-melodious-crab.glitch.me";

url3="https://glitchyyb.deno.dev";

url4="https://ggyyb.deno.dev";

headers2={
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "Cache-Control": 'no-cache',
            "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5 Plus Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2899 MMWEBSDK/201001 Mobile Safari/537.36 MMWEBID/1486 MicroMessenger/7.0.20.1781(0x27001439) Process/toolsmp WeChat/arm64 NetType/4G Language/zh_CN ABI/arm64",
"origin": "https://prodev.m.jd.com",
            "accept": "*/*", 
            "connection": "Keep-Alive",
            "Accept-Encoding": "gzip,deflate"


            }

           
headers3={
           
"User-Agent": "Mozilla/5.0 (Linux; Android 7.0; SLA-AL00 Build/HUAWEISLA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2898 MMWEBSDK/191102 Mobile Safari/537.36 MMWEBID/4984 MicroMessenger/7.0.9.1560(0x27000933) Process/tools NetType/WIFI Language/zh_CN ABI/arm32",  
 "Host": "api.m.jd.com",
    "content-type": "application/x-www-form-urlencoded",
    "accept": "application/json, text/plain, */*",

    "origin": "https://prodev.m.jd.com",
    "x-requested-with": "com.tencent.mm",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "referer":"https://prodev.m.jd.com",
"accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",

        "Accept-Encoding": "gzip,deflate",
"x-rp-client": "h5_1.0.0",

"x-referer-page": "https://prodev.m.jd.com",
"cookie":"b_webp=1;b_avif=0;shshshfpa=56443212-17d3-87c6-33b6-12712801fea9-1686831977;shshshfpx=56443212-17d3-87c6-33b6-12712801fea9-1686831977;share_cpin=;share_open_id=;share_gpin=;channel=;source_module=;erp=;retina=1;appCode=msd95910c4;webp=1;shareChannel=;buy_uin=6318741733;jdpin=jd_HcVilmGHPXiq;mcossmd=eab74d73079040de9b5b5ed2d1e92677;open_id=oTGnpnHoEUBbB7mlAw-yWcdBlokQ;pin=jd_HcVilmGHPXiq;pinId=sSK7fPguPoQQa2jo2BZrmw;wq_unionid=oCwKwuBH0w7AOfaXuOe2LzRwSEYc;wx_nickname=jd_user;visitkey=66958198491601686831238351;wxapp_openid=oA1P50AoTfxs1hAz7xRwSiXD0EPM;wq_addr=10678464405|13_1042_1048_54535|%E5%B1%B1%E4%B8%9C_%E7%83%9F%E5%8F%B0%E5%B8%82_%E8%93%AC%E8%8E%B1%E5%8C%BA_%E5%8D%97%E7%8E%8B%E8%A1%97%E9%81%93|%E5%B1%B1%E4%B8%9C%E7%83%9F%E5%8F%B0%E5%B8%82%E8%93%AC%E8%8E%B1%E5%8C%BA%E5%8D%97%E7%8E%8B%E8%A1%97%E9%81%93%E5%AF%A8%E9%87%8C%E6%9D%9116|120.791998%2C37.772414;__jdc=122270672;block_call_jdapp=11;defaultHeadId=;gHeadAddressId=;gHeadPlanId=;gSId=;gDSId=;buildtime=20230915;mba_muid=168802646502965216362;b_dw=400;b_dh=673;b_dpr=1.7999999523162842;rurl=https%3A%2F%2Fcoupon.m.jd.com%2Fcoupons%2Fshow.action%3Fkey%3Dcam8cfs7o9ae4f60be78425b2e2bc7dd%26roleId%3D121160028;equipmentId=MM6FSQAGGVN376UXYEBUE62SPM54QNOVP6UOEWQKJ3BY7XW55JWUMJFBQ34SMSR4MZZPA4OHJQCMHSWIMP22IXEKXY;fingerprint=5a7d61e7c78bb33a5df382c6547ca317;deviceVersion=7.0.19.1740%280x27001310%29;deviceOS=android;deviceOSVersion=8.1.0;deviceName=WeiXin;TrackID=slZAX8Y1_WojgRW2zrZvutgq_q8U93kBXH9YKCtny62eXNR9Hg7KJBitCiFyv1jYv-KU4RuuI03AYnJT7f5bW3oG6fcjzTGEEDUF1RN6jKWxLB1aUTJTfZZTHzqNZY_Zkay_aKVqCngC5XOFwMwt03nAoFH2M9Grck6P2egfVIA;nickname_base64=;openid2=C1B57B73D5D3A1E6615515F5D553047030D09E487065EDE69E932644BED5A0FF91F9F4D87C4E47F050708ACD568D5FE2;picture_url=;pinsign=2dc0a6f28dc1bef6f440d58396a64a1f;sex=0;wq_skey=zaAD8EBEFF01F385EAA4C203977E341D250F4B64528240143F52347E07EFE0FE4F643D757CD2F49FC1D2BF6C0BFD4F74BAA2871A19E32DF5F22EFEB834B0D2D2991AA8D82799F69A45670B7B0320165A2C;wq_uin=6318741733;cid=9;__jdv=122270672%7Cdirect%7C-%7Cnone%7C-%7C1697132650762;__wga=1697132652063.1697132652063.1696349676661.1686831241821.1.25;3AB9D23F7A4B3C9B=Z3W4XZZNJNX7YVONVYO3EJ7MCJKEQU2WR26GBSZQNBOY2TBZ5F4RIUCSDS7C5PA6F3QA2SFH3LXIHQ2324CLLA4WNE;__jda=122270672.943269572755159d8a087902a3f98895.1695156927.1697647739.1697808350.8;3AB9D23F7A4B3CSS=jdd03Z3W4XZZNJNX7YVONVYO3EJ7MCJKEQU2WR26GBSZQNBOY2TBZ5F4RIUCSDS7C5PA6F3QA2SFH3LXIHQ2324CLLA4WNEAAAAMLJVBYNMYAAAAADZIGEGXCEXRYAMX;_gia_d=1;network=wifi;TrackerID=AuVi68Y_Fe5KrpIq6GabezF0A0g4GX15Xasb7DAzzf906B1lhMQ5BHUmr5TAqcbu0VjazVbSTbECbgelleLxeFN-7RjDjFFGRa4O3hy8KKlgmRp7F7OWT1xztBmWBEU09xQuosoH_49Ibw0z4y5vdw;pt_key=AAJlMn_8ADApwprYBcE1pj0MSOgknz_11psa_bTQ1MFFEa08yd5f-yr1ohanE5oSSrUtmu-kIF8;pt_pin=jd_HcVilmGHPXiq;pt_token=4ag4gbpe;pwdt_id=jd_HcVilmGHPXiq;sfstoken=tk01ma0611c26a8sMSsyeDJ4M2NKy+7+NXt2qAi4kYJYdqF4Jcaf3Xxy7eklBW6hIelsZWVjwCwAQdfrg0tX9K63RUbZ;__jdb=122270672.2.943269572755159d8a087902a3f98895|8.1697808350;mba_sid=16978083504937164033790364426.2;__jd_ref_cls=MDownLoadFloat_TopOldExpo;joyytokem=babel_2vsLWSF6ktmQqVxTrwGMt4iN3tz3MDFtam9hSDk5MQ==.XFxWVnBdUlxYeV5ZVx8NO1IWU35YP1xTNlxGWU15QVsRUzZcFC4gJSoCPlF6IS8EMDEoAgk1IFUzFRUgJxIkIABAGz0ADwoSA1IbCisuIAksFBE=.12980afb;shshshfpb=AAu4rRE2LEkQyEhfTh8YzthJxKAH-qRaGgxl3SgAAAA9qZF9IY1ZpbG1HSFBYaXE;joyya=1697808384.1697808397.72.1druzyd;"
           
      
            }

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

"dnt": "1",
           "cookie":"b_webp=1;b_avif=1;appCode=msd95910c4;jdpin=gibaoxi;open_id=oTGnpnPA5IQ1FUGWMjkM-um5Ze2E;pin=gibaoxi;wx_nickname=jd_user;commonAddress=6065843065;regionAddress=13%2C1042%2C1048%2C54535;shshshfpx=677a6cc1-ce32-5ba7-a69e-b60e347828eb-1675164635;visitkey=11081520779461678240283221;wxapp_openid=oA1P50GPWXs3CuodUL4M3vaglu-k;wq_addr=11027481485%7C13_1042_1048_54535%7C%u5C71%u4E1C_%u70DF%u53F0%u5E02_%u84EC%u83B1%u533A_%u5357%u738B%u8857%u9053%7C%u5C71%u4E1C%u70DF%u53F0%u5E02%u84EC%u83B1%u533A%u5357%u738B%u8857%u9053%u534A%u5C9B%u84DD%u5EAD%28%u5357%u738B%u6751%u534A%u5C9B%u5170%u4EAD%29%u5357%u738B%u6751%7C120.807972%2C37.789425;shshshfpa=677a6cc1-ce32-5ba7-a69e-b60e347828eb-1675164635;share_cpin=;share_open_id=;share_gpin=;channel=;source_module=;erp=;wxapp_uuid=16782402830862067149;webp=1;shareChannel=;buy_uin=5313646889;mcossmd=2776247380e2a456880c18047c86a7ed;pinId=BjKFPOI-81I;wq_unionid=oCwKwuCcHLNS0kRmrNyNZIq16s0Q;e_wq_addr=CJOmCtc0ENO0ENUvD0CnC18nCNGyXzOmDNrpDJG1CzUvD0CvdJVNDzOvdJHPCUDpTXU3COHQTXU1C0YmTXU1HJKyXyV1ENHPGyV1ENDMCIV1DJCzGV8vdJUzDJcvdJczEOSvdJq4DJcvdJumDJCvD0CvdJVNDzOvdJHPCUCvdJcmHOYvdJUzHtKvdJVPCNSvdJq0HUCvdJqzGtOvdJUzC0OvdJUzDJcvdJczEOSvdJq4DJcvdJumDJCvdJUzDOOvdJVNEUSvdJq0HOGvdJVPGUGvCtqvdJUzDJcvdJczEOSvdJY3DJOvdJUzDOOvdJVNEUSvdJUnDzKvdJHPGUGvCtuvdJUzDJcvdJczEOSvdJY3DJOvD0CnCtKkENK3EJcyTJTNCzckDzq5DNS1;b_dw=400;b_dh=745;b_dpr=2.700000047683716;shshshfpb=ldm_5s3eJuwVEQe9KPKSA3w;__jdu=8b1d80804fdcc7b21d769e0730aa46ca;qid_uid=d225db8c-8efd-466a-a510-b2ae8340a285;qid_fs=1697701266108;qid_ls=1697701266108;qid_ts=1697701266160;qid_vis=1;pt_pin=gibaoxi;pwdt_id=gibaoxi;TrackerID=XtDAwhLw8734c7Xse1jXp_BDMIzdf1Wp3uzpyfOH8wofo-hrwgc4YbrZN1tBOvpWFCHnLMzrWXzwjWJeyPcwdeMFObRm9oI-W_bPkl-osQy1gkgG3qwRandM2ZBYjwFi;pt_key=AAJlMN3QADD9ZQ2-_cV6XZcQn0gMOduewHdp-AQuM66PsAzOLMMzv1EqQQZKZzDXXGWNlnYT0FY;pt_token=ag974jfj;retina=1;__wga=1697791347465.1697791001475.1697700891380.1696071661230.70.3;PPRD_P=EA.17078.79.1-CT.137081.10.1-UUID.83982c14ea7541fbc87f6b6d546411e7-LOGID.1697791347480.1244462744;pinStatus=0;wxapp_version=8.22.180;buildtime=20231018;__jdc=122270672;__jdwxapp=16782402830862067149.JA2019_5112348.wx91d27dbf599dff74.;3AB9D23F7A4B3CSS=jdd03C63JYUTJGNWNJVI4IFVJWN35SQCLGMTZO3GOIX2DOCTGVYWM7777Z5Y4FZK4QXZR4BD6JEWTRSQT465EXLO25DLYUYAAAAMLJRAKP4IAAAAADEZT6PGVWHLEEQX;3AB9D23F7A4B3C9B=C63JYUTJGNWNJVI4IFVJWN35SQCLGMTZO3GOIX2DOCTGVYWM7777Z5Y4FZK4QXZR4BD6JEWTRSQT465EXLO25DLYUY;equipmentId=C63JYUTJGNWNJVI4IFVJWN35SQCLGMTZO3GOIX2DOCTGVYWM7777Z5Y4FZK4QXZR4BD6JEWTRSQT465EXLO25DLYUY;fingerprint=b1a137d47cb28df9c8146ca9daf53166;deviceVersion=8.0.1840%280x28000036%29;deviceOS=android;deviceOSVersion=10;deviceName=WeiXin;rurl=https%3A%2F%2Fgt.m.jd.com%2Ffootprint%2Findex%3Fsource%3Dmini%26ptag%3D7155.1.10%26cookie%3D%257B%2522wxapp_type%2522%253A1%257D%23%26wxappSeries%3D%257B%2522uuid%2522%253A%252216782402830862067149%2522%252C%2522std%2522%253A%2522JA2019_5112348%2522%252C%2522seq%2522%253A45%252C%2522vts%2522%253A44%252C%2522appid%2522%253A%2522wx91d27dbf599dff74%2522%257D;TrackID=BppMoQvL1vCYkLIDkfcFV5QUS4MOVAiDP98LgYoUJRZVGQDhK5STpImUpOi0UZ6n7RjoRg1eLc2okSIyYJ0c3UHipJWM3u2wVUQTgzK1ELJ0178BXhiDwtZPhpWqZEHSx_PrUz0Rkd8fvPx4wrf7ZTyMBxD0nMxdogUG5oM6XS0;nickname_base64=;openid2=2DD50BB572E0FEA29A977A6FF681B040838C2EC1A470009E37EE5579BAE16A6892015F7BC6570094F1B1B3E0A8F33C2C;picture_url=;pinsign=7a99a6955da168fc09196b50abfa241d;sex=0;wq_skey=za6235B14C9645BEA46619C09A75FFDFE8669EBCA7BFB4156314C56BF5EB5C9DC7EB337521588CD53C1363A3CCDAA06EFA438BF851828C733BEC7BE5DF0FEC92BA67490B9CDD05F108D21AA0E231473F90;wq_uin=5313646889;country=;sfstoken=tk01wc4d11c99a8sMngxeDIrMisztzNfqU0PN67j68eb6K8NrcM9YOB1POg2LxFbDmQ4fNURNWlHwVdWfWuW6lGtKnjV;cid=5;wxapp_type=1;__jd_ref_cls=MFootPrintFloat_ListPro;__jda=122270672.52aa19b289adf22d349d72bdc3ff4a68.1697700891.1697700891.1697889424.2;mba_muid=83982c14ea7541fbc87f6b6d546411e7;wq_auth_token=328EF55559FF79DAD216C036FAD722C32CF6D88D08AC2DFF796F66AF5B0AD64C;__jdb=122270672.3.52aa19b289adf22d349d72bdc3ff4a68|2.1697889424;__jdv=122270672%7Cweixin%7Ct_1000072662_17005_001%7Cweixin%7Cdzh_h5_Menu_Fanswelfare_101%7C1697890415515;" 
           
    }
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
notice(response1.text+response2.text+response3.text+response4.text+response5.text+response6.text+response7.text+response8.text)  

