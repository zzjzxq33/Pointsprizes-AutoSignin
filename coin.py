import json
import os
import requests

vlist_headers = {
	'Host': 'api.bilibili.com',
	'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0',
	'Accept': 'application/json, text/plain, */*',
	'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
	'Accept-Encoding': 'gzip, deflate, br',
	'Origin': 'https://space.bilibili.com',
	'DNT': '1',
	'Connection': 'keep-alive',
	'Referer': 'https://space.bilibili.com/456664753/video',
	'Cache-Control': 'max-age=0',
	'TE': 'Trailers'
}
PostCoin_headers = {
	'Host': 'api.bilibili.com',
	'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0',
	'Accept': 'application/json, text/plain, */*',
	'Accept-Language': 'h-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
	'Accept-Encoding': 'gzip, deflate, br',
	'Content-Type': 'application/x-www-form-urlencoded',
	'Content-Length': '94',
	'Origin': 'https://www.bilibili.com',
	'Connection': 'keep-alive',
	'Referer': 'https://www.bilibili.com/video/',
	'Cookie': '',
	'TE': 'Trailers'
}

res = requests.get('https://api.bilibili.com/x/space/arc/search?mid=456664753&ps=30&tid=0&pn=1&keyword=&order=pubdate&jsonp=jsonp',headers = vlist_headers)
vlist_text = json.loads(res.text)
print(vlist_text['data']['list']['vlist'][0]['aid'])
print(vlist_text['data']['list']['vlist'][1]['aid'])
print(vlist_text['data']['list']['vlist'][2]['aid'])
#powered by woshoxxx

