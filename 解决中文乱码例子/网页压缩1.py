import requests
url='http://www.sina.com.cn/'
r=requests.get(url)
print(r.text)