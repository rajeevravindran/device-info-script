import requests

url='http://192.168.0.104:8888/dynamic.json'
r=requests.get(url,params=None)
payload=r.json()
print payload
print payload['net_received']