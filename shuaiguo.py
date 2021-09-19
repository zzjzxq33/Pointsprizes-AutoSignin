import requests
import os
import time

headers = {
    "Accept": "*/*"
    "Accept-Encoding": "gzip, deflate, br"
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
    "Connection": "keep-alive"
    "Cookie":""
    "Host": "bbs.sgguo.com"
    "Referer": "https://bbs.sgguo.com/forum.php"
    "sec-ch-ua": '"Microsoft Edge";v="93", " Not;A Brand";v="99", "Chromium";v="93"'
    "sec-ch-ua-mobile": "?0"
    "sec-ch-ua-platform": "Windows"
    "Sec-Fetch-Dest": "empty"
    "Sec-Fetch-Mode": "cors"
    "Sec-Fetch-Site": "same-origin"
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52"
    "X-Requested-With": "XMLHttpRequest"
#    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
}

headers['Cookie'] = os.environ.get('shuaiguo_cookie')
res = requests.get('https://shuaiguo.club/home.php?mod=task&do=apply&id=1',headers = headers)

print(res.text)
time.sleep(10)
#res2 = requests.get('https://bbs.sgguo.com/k_misign-sign.html?operation=qiandao&format=global_usernav_extra&formhash=690ffce7&inajax=1&ajaxtarget=k_misign_topb',headers = headers)
#print(res2.text)
