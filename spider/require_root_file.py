import urllib.request

website = 'https://www.huya.com/g/lol'

web_info = urllib.request.urlopen(website)  # 获取原始网页
web_info = web_info.read().decode('utf-8')  # 对原网页进行解码
