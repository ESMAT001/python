import requests
import  socket
import json
import publicip


proxies = {
  'http': '103.126.4.53:80',
  'https': '78.140.201.254:11335',
}

key='74dbc85d8a3f5d3611b785016fd823c3'

url='https://jsonip.com/'

response= requests.get(url,proxies=proxies)
t=response.json()
response=requests.get(f"http://api.ipstack.com/{t['ip']}?access_key={key}")
t=response.json()
print(t)