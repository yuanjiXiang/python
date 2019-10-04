import urllib.request
import ssl

website = 'https://www.huya.com/g/lol'

context = ssl._create_unverified_context()

web_info = urllib.request.urlopen(website, context=context)  # 获取原始网页
web_info = web_info.read().decode('utf-8')  # 对原网页进行解码
