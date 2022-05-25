# MAC:
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import json
import os
import urllib.request

basedir = "google/3"
if not os.path.exists(basedir):
    os.makedirs(basedir)

url = "https://www.google.com/doodles/json/2022/3?hl=zh-TW"
response = urllib.request.urlopen(url)
# response有個method: .read()
# print(type(response.read()))
# 1. json.loads(response.read())
# 2. json.load(response)
pics = json.load(response)
# print(type(pics))
for p in pics:
    print(p["title"])
    imgurl = "https:" + p["url"]
    print(imgurl)
    print("-" * 30)
    fn = imgurl.split("/")[-1]
    fn = os.path.join(basedir, fn)
    urllib.request.urlretrieve(imgurl, fn)