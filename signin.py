import requests
import os

headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': '', 
    'referer': 'https://www.pointsprizes.com/account',
    'sec-ch-ua': '%22Google%20Chrome%22%3Bv%3D%2287%22%2C%20%22%20Not%3BA%20Brand%22%3Bv%3D%2299%22%2C%20%22Chromium%22%3Bv%3D%2287%22',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}

headers["cookie"] = os.environ.get('cookie');
uid = os.environ.get('uid');

url = 'https://www.pointsprizes.com/account/earn/poll/' + uid + "?account_earn_poll_submit=1&poll_source=Not%20Telling&poll_source_website=&poll_site_speed=5&poll_customer_service=5&poll_ease_of_use=5&poll_feedback="

res = requests.get(url, headers=headers)
print(res.text)