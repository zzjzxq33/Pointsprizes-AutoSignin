import requests
import os

headers = {
    'Host': 'shuaiguo.club',
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://shuaiguo.club/home.php?mod=task',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': ''
}

headers['Cookie'] = os.environ.get('shuaiguo_cookie')
res = requests.get('https://shuaiguo.club/home.php?mod=task&do=apply&id=1',headers = headers)

print(res.text)
res2 = requests.get('https://shuaiguo.club/home.php?mod=task&do=draw&id=1 ',headers = headers)
print(res2.text)